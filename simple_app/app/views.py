from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import time
import random


"""Root endpoint"""
@require_http_methods(["GET"])
def home(request):
    
    return JsonResponse({
        'message': 'DevOps Test API',
        'version': '1.0.0',
        'endpoints': {
            'api': '/api/',
            'slow': '/slow/',
            'metrics': '/metrics/',
            'webhook': '/webhook/'
        },
        'timestamp': time.time()
    })

"""Healthy endpoint"""
@require_http_methods(["GET"])
def api_endpoint(request):
    # Simulate some processing time
    time.sleep(random.uniform(0.1, 0.5))
    
    return JsonResponse({
        'message': 'Hello from Django API!',
        'timestamp': time.time(),
        'version': '1.0.0'
    })


"""Slow endpoint"""
@require_http_methods(["GET"])
def slow_endpoint(request):
    # Simulate a slow endpoint for testing alerts
    time.sleep(2)
    return JsonResponse({
        'message': 'This is a slow endpoint',
        'processing_time': '2 seconds'
    })
# Create your views here.
