from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def vendor(request):
    return render(request, 'vendor.html')


def purchase(request):
    return render(request, 'purchase.html')


def tech(request):
    return render(request, 'tech.html')


def production(request):
    return render(request, 'production.html')


def admin(request):
    return render(request, 'admin.html')
