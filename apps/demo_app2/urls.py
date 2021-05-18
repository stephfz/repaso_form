from django.urls import path, include
from apps.demo_app2 import views

urlpatterns = [
    path('', views.index),
]
