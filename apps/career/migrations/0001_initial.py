# Generated by Django 5.1.6 on 2025-02-20 20:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='Nivel')),
                ('short_name', models.CharField(max_length=5, verbose_name='Nombre corto')),
            ],
            options={
                'verbose_name': 'Nivel',
                'verbose_name_plural': 'Niveles',
            },
        ),
        migrations.CreateModel(
            name='Quarter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quarter', models.IntegerField(verbose_name='Cuatrimestre No.')),
                ('quarter_name', models.CharField(max_length=25, verbose_name='Cuatrimestre')),
            ],
            options={
                'verbose_name': 'Cuatrimestre',
                'verbose_name_plural': 'Cuatrimestres',
            },
        ),
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('short_name', models.CharField(max_length=10, verbose_name='Nombre corto')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
                ('year', models.CharField(max_length=5, verbose_name='Año')),
                ('principal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Director')),
                ('level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='career.level', verbose_name='Nivel')),
            ],
            options={
                'verbose_name': 'Carrera',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Materia')),
                ('total_hours', models.IntegerField(verbose_name='Horas totales')),
                ('weekly_hours', models.IntegerField(verbose_name='Horas por semana')),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='career.career', verbose_name='Carrera')),
                ('quarter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='career.quarter', verbose_name='Cuatrimestre')),
            ],
            options={
                'verbose_name': 'Materia',
            },
        ),
    ]
