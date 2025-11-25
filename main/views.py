from rest_framework import viewsets, permissions
from .models import Usuario, Troca, Planta, Imagem, Mensagem, Avaliacao
from .serializers import (
    UsuarioSerializer, 
    TrocaSerializer, 
    PlantaSerializer, 
    ImagemSerializer, 
    MensagemSerializer, 
    AvaliacaoSerializer
)

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
    # Permite acesso irrestrito para facilitar o teste com o banco legado
    permission_classes = [permissions.AllowAny]


class PlantaViewSet(viewsets.ModelViewSet):
    queryset = Planta.objects.all()
    serializer_class = PlantaSerializer
    # Como não temos autenticação vinculada, deixamos AllowAny para testes
    permission_classes = [permissions.AllowAny] 

    # Removido perform_create pois não há vínculo automático com request.user
    # O frontend deve enviar o "usuario": ID no JSON.


class TrocaViewSet(viewsets.ModelViewSet):
    queryset = Troca.objects.all()
    serializer_class = TrocaSerializer
    permission_classes = [permissions.AllowAny]


class ImagemViewSet(viewsets.ModelViewSet):
    queryset = Imagem.objects.all()
    serializer_class = ImagemSerializer
    permission_classes = [permissions.AllowAny]


class MensagemViewSet(viewsets.ModelViewSet):
    queryset = Mensagem.objects.all()
    serializer_class = MensagemSerializer
    permission_classes = [permissions.AllowAny]


class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    permission_classes = [permissions.AllowAny]