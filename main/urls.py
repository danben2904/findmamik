from django.urls import path, reverse_lazy
from django.conf.urls import url

from django.contrib.auth import views as auth_views

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.registerPage, name='register'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('user/<str:username>', views.userPage, name='user'),
    path('account', views.accountSettings, name='account'),
    path('find', views.find, name='find'),
]

