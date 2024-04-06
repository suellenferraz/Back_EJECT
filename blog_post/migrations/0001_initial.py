# Generated by Django 5.0.4 on 2024-04-05 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='fotos')),
                ('titulo', models.CharField(max_length=250)),
                ('descricao', models.TextField()),
                ('text_button', models.CharField(max_length=20)),
            ],
        ),
    ]