from django.contrib import admin


from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),

    
    path('change_password', views.changpw, name='changpw'),

    path('reset_password', views.resetpw, name='resetpw'),
    path('reset_password/<int:uid>/<str:token>', views.resetpw, name='resetpw_return'),


    path("", views.home, name='home'),


    path('lista', views.index, name='index'),
    path('lista/<int:page>', views.index, name='index_paged'),

    path('apagar/<int:id>', views.delete_user, name='delete_user'),
    path('apagar/<int:id>/c', views.delete_user, name='delete_user_confirm'),

    path('validar/<int:id>', views.validate_user, name='validate_user'),

    path('editar/<int:id>', views.edit_user, name='edit_user')
]