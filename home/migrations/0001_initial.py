# Generated by Django 5.0.3 on 2024-04-07 05:34

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Alunos",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("imagem", models.ImageField(upload_to="fotos_alunos")),
                ("nome", models.CharField(max_length=100)),
                ("curso", models.TextField()),
                ("avaliacao", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Bem_vindo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=200)),
                ("descricao", models.TextField()),
                ("texto_botao", models.CharField(max_length=20)),
                ("imagem", models.ImageField(upload_to="fotos_home")),
            ],
        ),
        migrations.CreateModel(
            name="Contato",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(max_length=254)),
                ("telefone", models.CharField(max_length=12)),
                ("facebook", models.CharField(max_length=100)),
                ("linkedin", models.CharField(max_length=100)),
                ("twitter", models.CharField(max_length=100)),
                ("instagram", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Cursos_mais_populares",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "imagem",
                    models.ImageField(upload_to="fotos_Curso", verbose_name="imagem"),
                ),
                ("titulo", models.CharField(max_length=50)),
                ("avaliacao", models.FloatField()),
                ("dados", models.TextField()),
                ("informacao", models.TextField()),
                ("valor_parcela", models.TextField()),
                ("valor_vista", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Nossa_historia",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("imagem", models.ImageField(upload_to="fotos_home")),
                ("titulo", models.CharField(max_length=50)),
                ("descricao", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Titulo_cursos_mais_populares",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=50)),
            ],
        ),
    ]
