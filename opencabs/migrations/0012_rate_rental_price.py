# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opencabs', '0011_booking_vehicle_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='rental_price',
            field=models.PositiveIntegerField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
