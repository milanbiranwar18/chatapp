from django.urls import path
from . import views

urlpatterns = [
    path('add_group/', views.add_group, name='add_group'),
    path('update/<int:id>/', views.update_group, name='update_group'),
    path('delete_group/<int:id>/', views.delete_group, name='delete_group'),
    path('home_page/', views.home_page, name='home_page'),
    path('add_members/<int:id>/', views.add_members, name= 'add_members'),
    path('view_group/<int:id>/', views.view_group, name= 'view_group'),
    path('delete_members/<int:id>/', views.delete_members, name='delete_members'),

    ]