# Generated by Django 3.0.7 on 2020-09-18 22:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_municipio', models.CharField(help_text='Informe o nome do município', max_length=100, null=True, verbose_name='Município')),
                ('lat', models.CharField(blank=True, help_text='Latitude', max_length=100, null=True, verbose_name='Latitude')),
                ('lon', models.CharField(blank=True, help_text='Longitude', max_length=100, null=True, verbose_name='Longitude')),
            ],
            options={
                'verbose_name': 'Município',
                'verbose_name_plural': 'Municípios',
                'ordering': ['-nome_municipio'],
            },
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_provincia', models.CharField(help_text='Informe o nome da província', max_length=100, null=True, verbose_name='Provincia')),
                ('lat', models.CharField(blank=True, help_text='Latitude', max_length=100, null=True, verbose_name='Latitude')),
                ('lon', models.CharField(blank=True, help_text='Longitude', max_length=100, null=True, verbose_name='Longitude')),
            ],
            options={
                'verbose_name': 'Província',
                'verbose_name_plural': 'Pronvíncias',
                'ordering': ['-nome_provincia'],
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_paciente', models.CharField(blank=True, help_text='Informe seu nome', max_length=100, null=True, verbose_name='Nome')),
                ('sobrenome', models.CharField(blank=True, help_text='Informe seu Sobrenome', max_length=100, null=True, verbose_name='Sobrenome')),
                ('birthdate', models.DateField(blank=True, help_text='Informe sua data de nascimento', null=True, verbose_name='Data de nascimento')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Criado em')),
                ('sexo', models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=20, null=True, verbose_name='Género')),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Municipio', verbose_name='Município')),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
                'ordering': ['nome_paciente'],
            },
        ),
        migrations.AddField(
            model_name='municipio',
            name='provincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Provincia', verbose_name='Província'),
        ),
        migrations.CreateModel(
            name='Caso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField(blank=True, help_text='Possiveis descrições sobre o caso', max_length=250, null=True, verbose_name='Descrição do Caso')),
                ('created_at', models.DateField(null=True, verbose_name='Criado em')),
                ('estado_caso', models.CharField(blank=True, choices=[('Positivo', 'Positivo'), ('Recuperado', 'Recuperado'), ('Morto', 'Morto')], max_length=50, null=True, verbose_name='Estado')),
                ('paciente', models.ForeignKey(help_text='Selecione o nome do paciente ', on_delete=django.db.models.deletion.CASCADE, to='core.Paciente', verbose_name='Paciente')),
            ],
            options={
                'verbose_name': 'Caso',
                'verbose_name_plural': 'Casos',
                'ordering': ['paciente'],
                'unique_together': {('estado_caso', 'paciente')},
            },
        ),
    ]
