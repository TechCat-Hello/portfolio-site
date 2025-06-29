from django.urls import path
from . import views


app_name = 'portfolio'

urlpatterns = [
    path('', views.home_view, name='home'),  
    path('apps/', views.project_list, name='apps_list'),  
    path('inventory-app/', views.inventory_detail_view, name='inventory_detail'),  
    path('contact/', views.contact, name='contact'),
    path('<slug:slug>/', views.project_detail, name='project_detail'),  # slugによる詳細ページ
    path('quake_viz/', views.quake_detail_view, name='quake_detail'),
    path('co2_viz/', views.co2_detail_view, name='co2_detail'),
]
