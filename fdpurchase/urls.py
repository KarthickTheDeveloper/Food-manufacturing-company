from django.urls import path
from . import views

urlpatterns = [
    path('purchase/', views.purchase),
    path('purchase/signup/', views.register),
    path('purchase/signin/', views.login)
]
