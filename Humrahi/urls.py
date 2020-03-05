from django.contrib import admin
from django.urls import path,include
from . import views

app_name:'Humrahi'

urlpatterns=[
    path('',views.index,name="index"),
    path("register/",views.register,name="register"),
    path("login/",views.login,name='login') ,
    path("logout/",views.logout,name='logout'),
    path('oauth/',include('social_django.urls'),name='social')
]