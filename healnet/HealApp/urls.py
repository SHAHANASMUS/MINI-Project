from django.contrib import admin
from django.urls import path
from HealApp import views

urlpatterns = [
    path('', views.home),
    path('login/', views.login_page, name='login'),
    path('patient_home', views.patient_home,name='patient_home'),
    path('general_home', views.general_home,name='general_home'),
    path('register/', views.register,name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('create_blog/', views.create_blog, name='create_blog'),
    path('search_blogs/', views.search_blogs, name='search_blogs'),
    path('view_blogs/', views.view_blogs, name='view_blogs'),
    path('messages/', views.messages, name='messages'),
    path('connection_requests/', views.connection_requests, name='connection_requests'),
    path('edit/<int:blog_id>/', views.edit_blog, name='edit_blog'),
    path('delete/<int:blog_id>/', views.delete_blog, name='delete_blog'),


]