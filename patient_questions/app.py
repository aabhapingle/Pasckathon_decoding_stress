import numpy as np
import flask
import pickle
from flask import Flask, render_template, request, jsonify

# initialise the flask app
app = Flask(__name__)
model = pickle.load(open('mcq.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
     if request.method == 'POST':
        data = request.json
        return jsonify(data)
        int_features = [int(x) for x in jsonify(data)]
        final_features = [np.array(int_features)]
        prediction = model.predict(final_features)

    output = prediction[0]

    return render_template('index.html', prediction_text='Your stress level is: {}'.format(output))

# @app.route('/predict_api', methods = ['POST'])
# def predict_api():
    

if __name__ == "__main__":
    app.run(debug=True)




