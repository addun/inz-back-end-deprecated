# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Node(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='children')
    name = models.CharField(max_length=150)

    def __unicode__(self):
        return self.name
