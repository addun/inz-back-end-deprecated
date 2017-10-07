# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.
from django.utils.safestring import mark_safe
from providers.models import Firm


class Machine(models.Model):
    name = models.CharField(max_length=50)
    provider = models.ForeignKey(to=Firm)

    def __unicode__(self):
        return self.name


class Extend(models.Model):
    machine = models.ForeignKey(to=Machine, on_delete=models.CASCADE)
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=150)


class Image(models.Model):
    machine = models.ForeignKey(to=Machine, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='machinery/')

    def image_preview(self):
        return mark_safe(u'<a href="%s"><img src="%s" width=150 /></a>' % (self.image.url, self.image.url))
