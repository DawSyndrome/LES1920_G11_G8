"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
from django.conf.urls import include, url
app_name = "main"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("inscricao/", views.inscricao, name="inscricao"),
    #path("login/", views.login, name="login"),
    path("register_col/", views.register_col, name="register_col"),
    path("update_col/<int:pk>/", views.update_col, name="update_col"),
    path("apagar_col/<int:pk>/", views.apagar_col, name="apagar_col"),
    path("ver_col/<int:pk>/", views.ver_col, name="ver_col"),

    path("register_ind/", views.register_ind, name="register_ind"),

    path("inscricao_col/", views.inscricao_col, name="inscricao_col"),
    path("inscricao_ind/", views.inscricao_ind, name="inscricao_ind"),

    path('view_forms/', views.view_forms, name='view_forms'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
   
]
