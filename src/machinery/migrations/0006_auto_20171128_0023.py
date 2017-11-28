# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-28 00:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machinery', '0005_auto_20171128_0008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='measuringcapability',
            name='content_type',
        ),
        migrations.AddField(
            model_name='machinetoolelement',
            name='measuring_accuracy',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='machinetoolelement',
            name='measuring_description',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='machinetoolrequirement',
            name='measuring_accuracy',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='machinetoolrequirement',
            name='measuring_description',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='machinetoolrequirement',
            name='maximum_displacement_error_of_linear_axis',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='machinetoolrequirement',
            name='maximum_repeatability_error_of_linear_axis',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='machinetoolrequirement',
            name='number_of_axes',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='machinetoolrequirement',
            name='number_of_simultaneous_axes',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.DeleteModel(
            name='MeasuringCapability',
        ),
    ]
