from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('sign-up/', views.register, name='sign-up'),
    
    path('client/', views.client, name='client'),
    path('fuelquoteform/', views.fuelquoteform, name='fuelquoteform'),
    path('fuelquotehistory/', views.fuelquotehistory, name='fuelquotehistory'), 
]