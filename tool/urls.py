# tool/urls.py
from django.urls import path
from .views import grapetree_view

urlpatterns = [
    path('', grapetree_view, name='grapetree'),
    # Add other tool-specific views here
]