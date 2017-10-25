# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-21 17:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('machinery', '0002_machinetoolrequirements_automatically_pallet_changeable'),
    ]

    operations = [
        migrations.CreateModel(
            name='AxisCapability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_axes', models.CharField(max_length=15)),
                ('number_of_simultaneous_axes', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='PositioningCapability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maximum_displacement_error_of_linear_axis', models.CharField(max_length=15)),
                ('maximum_repeatability_error_of_linear_axis', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='RangeOfMotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('axis_name', models.CharField(max_length=15)),
                ('motion_range', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='positioningcapability',
            name='maximum_range_of_motion',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='machinery.RangeOfMotion'),
        ),
        migrations.AddField(
            model_name='machinetoolrequirements',
            name='axis',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='machinery.AxisCapability'),
        ),
        migrations.AddField(
            model_name='machinetoolrequirements',
            name='positioning',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='machinery.PositioningCapability'),
        ),
    ]
