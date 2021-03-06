# Generated by Django 3.1.1 on 2020-09-22 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sexo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50)),
                ('sigla', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Alunos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('dt_cadastro', models.DateTimeField(auto_now_add=True)),
                ('sexo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alunos.sexo')),
            ],
        ),
    ]
