from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_atividades, name='lista_atividades'),
    path('criar/', views.criar_atividade, name='criar_atividade'),
    path('<int:atividade_id>/responder/', views.responder_atividade, name='responder_atividade'),
    path('<int:atividade_id>/feedback/', views.feedback_atividade, name='feedback_atividade'),
]
