from django.urls import path
from . import views

urlpatterns = [
    path('', views.comunidade_lista, name='comunidade_lista'),
    path('criar/', views.criar_post, name='comunidade_criar'),
]
