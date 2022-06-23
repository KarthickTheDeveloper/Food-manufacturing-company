from django.urls import path
from . import views

urlpatterns = [
    path('tech/', views.tech),
    path('tech/signup/', views.register),
    path('tech/signin/', views.login)
]
