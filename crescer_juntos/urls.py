from django.contrib import admin
from django.urls import path, include
from main.views import health_check  # <--- Importante: Importar a view aqui

# Este arquivo define as rotas globais do projeto.
# Ele delega tudo que começa com 'api/' para o arquivo main/urls.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('main.urls')),  # Conecta as rotas do app 'main'
    
    # Adicionamos esta linha para o teste de saúde funcionar:
    path('health/', health_check, name='health_check'),
]