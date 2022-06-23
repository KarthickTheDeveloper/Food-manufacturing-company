from django.shortcuts import render, redirect
from fdvendor.models import Vendormodel
from .models import Purchasemodel
from django.contrib import messages
# from django.db import models
# Create your views here.


def purchase(request):
    return render(request, 'purchase/purchase.html')


def vendorlist(request):
    ven = Vendormodel.objects.all()
    return render(request, 'purchase/purchase.html', {'ven': ven})


def register(request):
    if request.method == 'POST':
        username = request.POST["user-name"]
        email = request.POST["email"]
        password = request.POST["password1"]
        repeatpassword = request.POST["password2"]
        phone = request.POST["mobile"]
        if password == repeatpassword:
            pur = Purchasemodel(name=username,mail=email,password=password,phone=phone).save()
            messages.info(request, 'Successfully Registered')
            return redirect('/purchase/signup/')
        else:
            messages.error(request, 'Passwords should be same!!!')
    return render(request, 'purchase/rl/index.html')


def login(request):
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password1"]
        # print(email)
        # print(password)
        try:
            pur = Purchasemodel.objects.get(mail=email)
            messages.success(request, "Login Success")
            return redirect('/purchase/')
        except:
            messages.error(request, "Given details not found")
            return redirect('/purchase/signin/')
    return render(request, 'purchase/rl/index.html')


