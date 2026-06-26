from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
# Create your views here.

def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'Home.html')

def product(request):
   return render(request,'Product.html')

def about(request):
    return render(request,'About.html')

def add_user(request):
    if request.method == "POST":
        f = UserForm(request.POST,request.FILES)

        if f.is_valid():
            f.save()
            return redirect('/users')
        else: 
            print(f.errors)
    else:
        f =  UserForm() 
    return render(request,'Add_products.html',{"f" : f})

# https methods POST , GET , PUT , PATCH , DELETE

def users(request):
    user = UserModel.objects.all()
    return render(request,'Users.html',{"Users":user})

def update_user(request , id):
    user = UserModel.objects.get(id = id)
    if request.method == "POST":
        f = UserForm(request.POST,request.FILES,instance=user)

        if f.is_valid():
            f.save()
            return redirect('/users')
        else: 
            print(f.errors)
    else:
        f =  UserForm(instance=user) 
    return render(request,'Update.html',{"form" : f})

def delete_user(request , id):
    user = UserModel.objects.get(id = id)
    user.delete()
    return redirect('/users')