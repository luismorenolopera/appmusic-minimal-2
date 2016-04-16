# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver


class Document(models.Model):
    docfile = models.FileField(upload_to='documents/music')


@receiver(pre_delete, sender=Document)
def mymodel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.docfile.delete(False)
