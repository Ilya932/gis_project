from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('test', views.test, name='test'),
    path('create/', views.create_client, name='create'),
]