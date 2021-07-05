from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/login/', views.loginUser, name='login'),
    path('accounts/register/', views.registerUser, name='register'),
    path('accounts/logout/', views.logoutUser, name='logout')
]
