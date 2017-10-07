# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Firm(models.Model):
    name = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
