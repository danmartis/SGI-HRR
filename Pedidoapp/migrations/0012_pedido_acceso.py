# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-27 20:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pedidoapp', '0011_articulo_total_pedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='acceso',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
