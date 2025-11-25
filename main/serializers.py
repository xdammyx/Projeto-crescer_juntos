from rest_framework import serializers
from .models import Usuario, Troca, Planta, Imagem, Mensagem, Avaliacao

class UsuarioSerializer(serializers.ModelSerializer):
    # O campo no banco é 'senha' (varchar 15). 
    # Definimos write_only=True para que a senha não seja exposta no JSON de resposta.
    senha = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = Usuario
        # Campos mapeados exatamente conforme seu SQL
        fields = ['id_usuario', 'nome', 'email', 'senha', 'localizacao', 'data_cadastro']
        read_only_fields = ['id_usuario', 'data_cadastro']

    def validate_email(self, value):
        # Verifica duplicidade na sua tabela personalizada 'usuarios'
        if Usuario.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este email já está em uso.")
        return value

    def create(self, validated_data):
        # Como seu banco tem uma tabela própria, salvamos direto nela.
        return Usuario.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome', instance.nome)
        instance.localizacao = validated_data.get('localizacao', instance.localizacao)
        instance.email = validated_data.get('email', instance.email)
        
        senha = validated_data.get('senha')
        if senha:
            instance.senha = senha
            
        instance.save()
        return instance


class TrocaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Troca
        # CORREÇÃO: Removido 'planta' pois a tabela SQL de trocas não tem esse campo
        fields = ['id_troca', 'data', 'status', 'usuario']
        # CORREÇÃO: 'usuario' removido de read_only para que o frontend envie o ID do dono
        read_only_fields = ['id_troca'] 


class PlantaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planta
        fields = [
            'id_planta', 'nome_popular', 'tipo', 'origem', 
            'familia', 'descricao', 'imagem', 'usuario'
        ]
        # CORREÇÃO: 'usuario' deve ser enviável pelo frontend
        read_only_fields = ['id_planta']


class ImagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagem
        fields = ['id_imagem', 'url_imagem', 'planta']
        read_only_fields = ['id_imagem']


class MensagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mensagem
        fields = ['id_chat', 'mensagem', 'usuario', 'data_hora']
        # CORREÇÃO: 'usuario' removido de read_only
        read_only_fields = ['id_chat', 'data_hora']


class AvaliacaoSerializer(serializers.ModelSerializer):
    # Mapeamento dos relacionamentos (Quem é avaliado e Quem avalia)
    id_avaliado = serializers.PrimaryKeyRelatedField(
        source='avaliado', 
        queryset=Usuario.objects.all(),
        error_messages={"does_not_exist": 'ID de usuário avaliado inválido.'}
    )
    
    # Adicionado: Necessário para saber QUEM está avaliando
    id_avaliador = serializers.PrimaryKeyRelatedField(
        source='avaliador',
        queryset=Usuario.objects.all(),
        error_messages={"does_not_exist": 'ID de avaliador inválido.'}
    )

    class Meta:
        model = Avaliacao
        fields = ['id_avaliacao', 'id_avaliador', 'id_avaliado', 'nota', 'comentario', 'data_hora']
        read_only_fields = ['id_avaliacao', 'data_hora']