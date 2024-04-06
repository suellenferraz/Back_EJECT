from django.db import models

# Create your models here.
class Blog(models.Model):
    image = models.ImageField(upload_to='fotos')
    titulo = models.CharField(max_length=250)
    descricao = models.TextField()
    text_button = models.CharField(max_length=20)
    