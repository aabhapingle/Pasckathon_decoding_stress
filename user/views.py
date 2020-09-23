from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from .models import Profile

def welcome(request):
    return render(request, 'user/welcome.html')
def usersignup(request) :
    if request.method == 'POST' :
        try :
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            user = User.objects.create_user(username=username, password=password)
            profile = Profile (user=user,email=email ,username=username, name=name, phone=phone )
            profile.save()
            print("efe")
            login(request, user)
            print("sde")
            return render (request, 'user/success.html')

        except :
            return render (request, 'user/home.html')

    elif request.method == 'GET' :
        print("dcfdhfui")
        return render (request, "user/home.html")
    return render(request,"user/home.html")

def loginn(request):
    if request.method == 'POST':
        username = request.POST.get ('username')
        password = request.POST.get ('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request,"users/success.html")
        else:
            return render(request,"users/failure.html")
    elif request.method == 'GET':
        return render (request,"user/login.html")
    return render(request, "user/login.html")

def answer(request):
    print("skdhguw")
    if request.method=='POST':
        print("skdhguw11")
        one=request.POST.get('first')
        two = request.POST.get('second')
        three = request.POST.get('three')
        four = request.POST.get('fourth')
        five = request.POST.get('fifth')
        six = request.POST.get('six')
        seven = request.POST.get('seven')
        eight = request.POST.get('eight')
        nine = request.POST.get('nine')
        ten = request.POST.get('ten')
        eleven = request.POST.get('eleven')
        twelve = request.POST.get('twelve')
        total_score = one + two + three+ four+five+six+seven +eight + nine+ten+eleven+twelve
        return render (request,'user/sucess.html',context={'total_score' : total_score})
    if request.method == 'GET':
        print("skdhguw")
        return render(request,'user/sucess.html')
    return render(request, 'user/sucess.html')

def logout(request):
    return render(request, 'user/logout.html')