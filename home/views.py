from django.shortcuts import render

from .models import Bem_vindo, Titulo_cursos_mais_populares, Cursos_mais_populares, Nossa_historia, Alunos, Contato
# Create your views here.
def home(request):

    bem_vindo = Bem_vindo.objects.last()
    titulo_cursos = Titulo_cursos_mais_populares.objects.last()
    cursos_populares = Cursos_mais_populares.objects.all()
    nossa_historia = Nossa_historia.objects.last()
    alunos = Alunos.objects.all()
    contato = Contato.objects.last()

    context = {
        'bemVindo': bem_vindo,
        'titulo_curso': titulo_cursos,
        'cursos_populares':cursos_populares,
        'nossa_historia':nossa_historia,
        'alunos':alunos,
        'contato':contato


        
    }

    return render(request, "index.html", context)