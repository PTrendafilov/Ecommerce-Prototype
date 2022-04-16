from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User, auth
from ecommerce.models import *
from ecommerce.views import cart_dict, total_money
import re
# Create your views here.

  
def check(email):   
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
    if(re.search(regex,email)):   
        return True
    else:   
        return False


def login(request): 
    menu=Menu.objects.first()

    site=Site.objects.first()

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        print("Hello")
        return render(request,'login.html', {'menu':menu, 'site':site})
def register(request):
    menu=Menu.objects.first()

    site=Site.objects.first()
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        if check(email)==False:
            messages.info(request,'Please give a valid email!')
            return redirect('register')
        if len(password1)<6:
            messages.info(request,'Password must be larger than 6 symbols')
            return redirect('register')
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print('User created')
                return redirect('login')
                
        else:
            messages.info(request,'Passwords not matching.')
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html', {'menu':menu, 'site':site})
def logout(request):
    global cart_dict, total_money
    cart_dict={}
    total_money=0
    auth.logout(request)
    return redirect('/')