from django.urls import path
from . import views

urlpatterns = [
    path('', views.mensagens_lista, name='mensagens_lista'),
    path('enviar/', views.enviar_mensagem, name='enviar_mensagem'),
]
