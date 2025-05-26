from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('atividades/', include('atividades.urls')),
    path('comunidade/', include('comunidade.urls')),
    path('mensagens/', include('mensagens.urls')),
    path('', include('usuarios.urls')),  # redirecionar / para login ou perfil
]
