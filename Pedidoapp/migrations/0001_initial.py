# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 18:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('cod_experto', models.CharField(blank=True, max_length=999, primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=999)),
                ('descripcion', models.CharField(blank=True, max_length=999, null=True)),
                ('stock', models.CharField(blank=True, max_length=999)),
                ('extmin', models.CharField(blank=True, max_length=999, null=True)),
                ('extmax', models.CharField(blank=True, max_length=999, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Articulo_esp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pedidoapp.Articulo')),
            ],
        ),
        migrations.CreateModel(
            name='Bodega',
            fields=[
                ('cod_bodega', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Encargado',
            fields=[
                ('rut_encargado', models.CharField(blank=True, max_length=999, primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50)),
                ('articulos_esp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pedidoapp.Articulo_esp')),
                ('encargado', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Pedidoapp.Encargado')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_entrega', models.DateTimeField()),
                ('fecha_pedido', models.DateTimeField(auto_now_add=True, null=True)),
                ('cantidad', models.IntegerField(blank=True)),
                ('pendiente', models.CharField(blank=True, max_length=999, null=True)),
                ('estado', models.CharField(blank=True, default='pendiente', max_length=20)),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pedidoapp.Articulo_esp')),
                ('especialidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pedidoapp.Especialidad')),
            ],
        ),
        migrations.AddField(
            model_name='articulo',
            name='info_bodega',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Pedidoapp.Bodega'),
        ),
    ]
