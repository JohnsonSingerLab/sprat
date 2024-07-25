# example/urls.py
from django.urls import path
# from tool.views import index
from . import views


urlpatterns = [
    # path('', index),
     path('', views.index, name='index'),
]

