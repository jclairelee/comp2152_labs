from django.urls import path
from . import views

urlpatterns = [
     path('', views.hello), 
    path('hello/', views.hello, name='hello'),
]
