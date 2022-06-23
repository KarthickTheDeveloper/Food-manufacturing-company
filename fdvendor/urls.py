from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index),
    path('', views.vendor),
    path('sign/', views.register, name="register"),
    # path('sign/', views.login),
    # path('purchase/', views.purchase),
    # path('tech/', views.tech),
    # path('production/', views.production),
    # path('admin1/', views.admin),
]
