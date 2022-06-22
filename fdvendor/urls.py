from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index),
    path('', views.vendor),
    path('register/', views.register),
    # path('purchase/', views.purchase),
    # path('tech/', views.tech),
    # path('production/', views.production),
    # path('admin1/', views.admin),
]
