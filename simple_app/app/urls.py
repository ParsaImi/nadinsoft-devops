from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/', views.api_endpoint, name='api_endpoint'),
    path('slow/', views.slow_endpoint, name='slow_endpoint'),
]
