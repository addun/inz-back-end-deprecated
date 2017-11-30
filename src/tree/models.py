# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Tree(models.Model):
    parent = models.OneToOneField('self', null=True, blank=True)
    name = models.CharField(max_length=150)
