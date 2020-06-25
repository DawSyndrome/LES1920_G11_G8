from django.urls import path
from . import views


app_name =  'utilizadores'
urlpatterns = [

    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
]