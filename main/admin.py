from django.contrib import admin
from .models import Usuario, Troca, Planta, Imagem, Mensagem, Avaliacao

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id_usuario', 'nome', 'email', 'localizacao', 'data_cadastro')
    search_fields = ('nome', 'email')

@admin.register(Troca)
class TrocaAdmin(admin.ModelAdmin):
    # REMOVIDO 'planta' pois não existe na tabela 'trocas' do seu SQL
    list_display = ('id_troca', 'data', 'status', 'usuario')
    list_filter = ('status',)

@admin.register(Planta)
class PlantaAdmin(admin.ModelAdmin):
    list_display = ('id_planta', 'nome_popular', 'tipo', 'familia', 'usuario')
    search_fields = ('nome_popular', 'familia')

@admin.register(Imagem)
class ImagemAdmin(admin.ModelAdmin):
    list_display = ('id_imagem', 'url_imagem', 'planta')

@admin.register(Mensagem)
class MensagemAdmin(admin.ModelAdmin):
    list_display = ('id_chat', 'usuario', 'data_hora')

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('id_avaliacao', 'nota', 'avaliador', 'avaliado', 'data_hora')