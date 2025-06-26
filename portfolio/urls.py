from django.urls import path
from . import views


app_name = 'portfolio'

urlpatterns = [
    path('', views.home_view, name='home'), 
    path('apps/', views.project_list, name='apps_list'), 
    path('contact/', views.contact, name='contact'),
]
