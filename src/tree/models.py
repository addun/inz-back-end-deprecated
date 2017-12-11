# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from machinery.models.machine_tool_requirement import MachineToolRequirement


class Node(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')
    value = models.CharField(max_length=150)

    def __unicode__(self):
        return self.value


class Tag(models.Model):
    node = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='tags')
    value = models.CharField(max_length=150)

    def __unicode__(self):
        return self.value


class TagMachineToolRequirement(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    machine_tool_requirement = models.ForeignKey(MachineToolRequirement, on_delete=models.CASCADE)
