from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='films'),
    path('create_film/', views.create_film, name='add_film'),
]
