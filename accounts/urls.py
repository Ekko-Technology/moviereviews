from django.urls import path
from . import views

urlpatterns = [
    # path to sign up page
    path('signupaccount', views.signupaccount, name='signup'),
    # path if users want to log in
    path('login/', views.loginaccount, name='login'),
    # path when users log out of or are not logged in into their account
    path('logout/', views.logoutaccount, name="logout"),
]