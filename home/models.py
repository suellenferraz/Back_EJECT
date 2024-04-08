from django.db import models

# Create your models here.
class Bem_vindo(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    texto_botao = models.CharField(max_length=20)
    imagem = models.ImageField(upload_to='fotos_home')

class Titulo_cursos_mais_populares(models.Model):
    titulo = models.CharField(max_length=50)

class Cursos_mais_populares(models.Model):
    imagem = models.ImageField(verbose_name="imagem", upload_to='fotos_Curso')
    titulo = models.CharField(max_length=50)
    avaliacao = models.FloatField()
    dados = models.TextField()
    informacao = models.TextField()
    valor_parcela = models.TextField()
    valor_vista =models.TextField()

    def __str__(self):
        return f'{self.titulo}'

class Nossa_historia(models.Model):
    imagem = models.ImageField(upload_to='fotos_home')
    titulo = models.CharField(max_length=50)
    descricao = models.TextField()

class Alunos(models.Model):
    imagem = models.ImageField(upload_to='fotos_alunos') 
    nome = models.CharField(max_length=100)
    curso = models.TextField()
    avaliacao = models.TextField()

    def __str__(self):
        return f'{self.nome}'


class Contato(models.Model):
    email = models.EmailField()
    telefone = models.CharField(max_length=12)
    facebook = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)