from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('room/', views.room, name='room'),
    path('', views.looby, name='looby'),
    path('get-token', views.getToken),

    path('create_member/', views.createMember),
    path('get_member/', views.getMember),
    path('delete_member/', views.deleteMember),
]
