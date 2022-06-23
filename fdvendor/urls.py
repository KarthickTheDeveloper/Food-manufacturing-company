from django.urls import path
from . import views

urlpatterns = [
    path('', views.vendor),
    path('signup/', views.register, name="register"),
    path('signin/', views.login, name="login"),
]
