from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),

    path('services/', views.service_list, name='service_list'),
    path('services/<slug:slug>/', views.service_detail, name='service_detail'),

    path('team/', views.team_list, name='team_list'),
    path('team/<slug:slug>/', views.team_detail, name='team_detail'),

    path('blogs/', views.blog, name='blog'),
    path('blogs/<str:pk>/', views.blog_detail, name='blog_detail'),

    ]