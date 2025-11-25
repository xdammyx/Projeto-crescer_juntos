from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=40)
    email = models.EmailField(unique=True, max_length=80)
    senha = models.CharField(max_length=100) 
    localizacao = models.CharField(max_length=100, blank=True, null=True)
    data_cadastro = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'usuarios'  # Conecta na tabela 'usuarios' do seu SQL
        managed = True         # O Django gerencia essa tabela

    def __str__(self):
        return self.nome


class Planta(models.Model):
    id_planta = models.AutoField(primary_key=True)
    nome_popular = models.CharField(max_length=40, blank=True, null=True)
    tipo = models.CharField(max_length=40, blank=True, null=True)
    origem = models.CharField(max_length=80, blank=True, null=True)
    familia = models.CharField(max_length=50, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    
    # Salva o arquivo na pasta 'media/plantas/' e o caminho (texto) no banco
    imagem = models.ImageField(upload_to='plantas/', max_length=150, blank=True, null=True)
    
    # db_column='id_usuario' garante que o Django use a coluna existente no SQL
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='id_usuario', related_name='plantas')

    class Meta:
        db_table = 'plantas'

    def __str__(self):
        return self.nome_popular if self.nome_popular else f"Planta {self.id_planta}"


class Imagem(models.Model):
    id_imagem = models.AutoField(primary_key=True)
    # O SQL pede url_imagem VARCHAR(150)
    url_imagem = models.ImageField(upload_to='detalhes/', max_length=150)
    planta = models.ForeignKey(Planta, on_delete=models.CASCADE, db_column='id_planta', related_name='imagens_extra')

    class Meta:
        db_table = 'imagens'


class Troca(models.Model):
    id_troca = models.AutoField(primary_key=True)
    data = models.DateField()
    status = models.CharField(max_length=15, blank=True, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='id_usuario')

    class Meta:
        db_table = 'trocas'


class Mensagem(models.Model):
    id_chat = models.AutoField(primary_key=True)
    mensagem = models.TextField()
    data_hora = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='id_usuario')

    class Meta:
        db_table = 'mensagens'


class Avaliacao(models.Model):
    id_avaliacao = models.AutoField(primary_key=True)
    nota = models.DecimalField(max_digits=3, decimal_places=1)
    data_hora = models.DateTimeField(auto_now_add=True)
    comentario = models.TextField(blank=True, null=True)
    
    avaliador = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='id_avaliador', related_name='avaliacoes_feitas')
    avaliado = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='id_avaliado', related_name='avaliacoes_recebidas')

    class Meta:
        db_table = 'avaliacao'