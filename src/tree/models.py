# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.
from machinery.models import Machine


class Node(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey(to='self', blank=True, null=True)
    machinery = models.ManyToManyField(to=Machine, blank=True)

    def __unicode__(self):
        return self.name
