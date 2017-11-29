# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-29 20:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('machinery', '0004_auto_20171129_1942'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spindlename',
            old_name='spindle_name',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='circularworktable',
            name='machine_tool_element',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='circularworktable', to='machinery.MachineToolElement'),
        ),
        migrations.AlterField(
            model_name='pallet',
            name='machine_tool_element',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pallet', to='machinery.MachineToolElement'),
        ),
        migrations.AlterField(
            model_name='partprobe',
            name='machine_tool_element',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partprobe', to='machinery.MachineToolElement'),
        ),
        migrations.AlterField(
            model_name='rectangularworktable',
            name='machine_tool_element',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rectangularworktable', to='machinery.MachineToolElement'),
        ),
        migrations.AlterField(
            model_name='spindle',
            name='machine_tool_element',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spindle', to='machinery.MachineToolElement'),
        ),
        migrations.AlterField(
            model_name='spindlename',
            name='turret',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spindle_names', to='machinery.Turret'),
        ),
        migrations.AlterField(
            model_name='straightspindle',
            name='machine_tool_element',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='straightspindle', to='machinery.MachineToolElement'),
        ),
        migrations.AlterField(
            model_name='taperedspindle',
            name='machine_tool_element',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taperedspindle', to='machinery.MachineToolElement'),
        ),
        migrations.AlterField(
            model_name='threadedspindle',
            name='machine_tool_element',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='threadedspindle', to='machinery.MachineToolElement'),
        ),
        migrations.AlterField(
            model_name='toolbreakage',
            name='machine_tool_element',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='toolbreakage', to='machinery.MachineToolElement'),
        ),
        migrations.AlterField(
            model_name='toolchanger',
            name='machine_tool_element',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='toolchanger', to='machinery.MachineToolElement'),
        ),
        migrations.AlterField(
            model_name='toolmagazine',
            name='machine_tool_element',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='toolmagazine', to='machinery.MachineToolElement'),
        ),
        migrations.AlterField(
            model_name='toolsetting',
            name='machine_tool_element',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='toolsetting', to='machinery.MachineToolElement'),
        ),
        migrations.AlterField(
            model_name='turret',
            name='machine_tool_element',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='turret', to='machinery.MachineToolElement'),
        ),
        migrations.AlterField(
            model_name='workspindle',
            name='machine_tool_element',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workspindle', to='machinery.MachineToolElement'),
        ),
    ]
