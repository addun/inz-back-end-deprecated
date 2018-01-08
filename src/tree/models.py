# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from enginery.models import MachineToolSpecification


class Node(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')
    value = models.CharField(max_length=150)

    def __unicode__(self):
        return self.value


class MachineToolSpecificationInNode(models.Model):
    node = models.ForeignKey(Node, on_delete=models.CASCADE)
    machine_tool_requirement = models.ForeignKey(MachineToolSpecification, on_delete=models.CASCADE)
