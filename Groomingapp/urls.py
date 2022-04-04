from django.contrib import admin
from django.urls import path,include
from Groomingapp import views

urlpatterns = [
    path('', views.home),
    path('profile/', views.profile, name='profile'),  
    path('services/', views.services, name='services'),
    path('required_details/', views.required_details, name='required_details'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('userlogout/', views.userlogout)
]