from django.urls import path
from . import views

urlpatterns = [
    path('', views.verification_Email, name='verification_Email'),  # Use this URL pattern
    # Add more URL patterns as needed
]