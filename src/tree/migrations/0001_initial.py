# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-09-22 13:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('machinery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MachineToolSpecificationInNode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_tool_requirement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='machinery.MachineToolSpecification')),
            ],
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=150)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='tree.Node')),
            ],
        ),
        migrations.AddField(
            model_name='machinetoolspecificationinnode',
            name='node',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tree.Node'),
        ),
    ]
