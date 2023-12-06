from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from CarApp import views
from CarApp.views import predict_price
from .views import CustomLoginView
from .views import CustomLogoutView

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('home/', views.home, name='home'),
    path('landingpage/', views.home, name='landingpage'),
    path("", views.landingpage, name='landingpage'),
    path("home", views.home, name='home'),
    path("home2", views.home2, name='home2'),
    path("about", views.about, name='about'),
    path("about2", views.about2, name='about2'),
    path("Egarage", views.Egarage, name='Egarage'),
    path("contact", views.contact, name='contact'),
    path("CarBuy", views.Carbuy, name='CarBuy'),
    path("CarSell", views.CarSell, name='CarSell'),
    path("CPP", views.CPP, name='CPP'),
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),
    path('predict_price/', predict_price, name='predict_price'),
]
    

    
    

