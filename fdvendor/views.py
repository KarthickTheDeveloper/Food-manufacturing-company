from django.shortcuts import render, redirect
from .models import Vendormodel
from django.contrib import messages
# Create your views here.
# def index(request):
#     return render(request, 'index.html')


def vendor(request):
    return render(request, 'vendor/vendor.html')


def register(request):
    if request.method == 'POST':
        vendorname = request.POST["vendor-name"]
        email = request.POST["email"]
        password = request.POST["password1"]
        repeatpassword = request.POST["password2"]
        itemname = request.POST["item-name"]
        itemquantity = request.POST["item-quantity"]
        if password == repeatpassword:
            ven = Vendormodel(vendorname=vendorname,email=email,password=password,itemname=itemname,itemquantity=itemquantity).save()
            messages.info(request, 'Successfully Registered')
            return redirect('/vendor/sign/')
        else:
            messages.error(request, 'Passwords should be same!!!')
    return render(request, 'vendor/rl/index.html')


# def login(request):
#     if request.method == 'post':
#         email = request.POST["email"]
#         password = request.POST["password1"]
#         print(email)
#         print(password)
#     return render(request, 'vendor/rl/index.html')

