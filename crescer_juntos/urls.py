from django.contrib import admin
from django.urls import path, include

# Este arquivo define as rotas globais do projeto.
# Ele delega tudo que começa com 'api/' para o arquivo main/urls.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('main.urls')),  # Conecta as rotas do app 'main'
]