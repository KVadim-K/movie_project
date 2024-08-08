from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='add_films'),
    path('new/', views.new, name='new_films'),
]
