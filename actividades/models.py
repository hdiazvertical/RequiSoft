from __future__ import unicode_literals
from django.db import models

class ReqParque(models.Model):
    codigo = models.CharField(max_length=200)
    descripcion = models.TextField()
    cumplido = models.BooleanField()

class ReqDgsm(models.Model):
    codigo = models.CharField(max_length=200)
    descripcion = models.TextField()
    cumplido = models.BooleanField()
    req_parque = models.ForeignKey(ReqParque)

class CasosDeUso(models.Model):
    codigo = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    req_dgsm = models.ManyToManyField(ReqDgsm)
