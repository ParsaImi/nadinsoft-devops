from django.urls import path
from . import views

urlpatterns = [
    path('health/', views.health_check, name='health_check'),
    path('api/', views.api_endpoint, name='api_endpoint'),
    path('slow/', views.slow_endpoint, name='slow_endpoint'),
]
