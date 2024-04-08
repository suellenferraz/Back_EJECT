from django.contrib import admin
from .models import Bem_vindo, Titulo_cursos_mais_populares, Cursos_mais_populares, Nossa_historia, Alunos, Contato

# Register your models here.

admin.site.register(Bem_vindo)
admin.site.register(Titulo_cursos_mais_populares)
admin.site.register(Cursos_mais_populares)
admin.site.register(Nossa_historia)
admin.site.register(Alunos)
admin.site.register(Contato)