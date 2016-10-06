from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class ReqDgsm(models.Model):
    codigo = models.CharField(max_length=200)
    descripcion = models.TextField()
    cumplido = models.BooleanField()

    class Meta:
        verbose_name_plural = 'Requisitos DGSM'

    def __str__(self):
        return self.codigo


class ReqParque(models.Model):
    codigo = models.CharField(max_length=200)
    descripcion = models.TextField()
    cumplido = models.BooleanField()
    req_dgsm = models.ForeignKey(ReqDgsm, null=True)

    class Meta:
        verbose_name_plural = 'Requisitos ParqueSoft'

    def __str__(self):
        return self.codigo


class CasosDeUso(models.Model):
    codigo = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    req_dgsm = models.ManyToManyField(ReqDgsm)

    class Meta:
        verbose_name_plural = 'Casos de Uso'

    def __str__(self):
        return self.codigo

class Actividades(models.Model):
    casos_de_uso = models.ManyToManyField(CasosDeUso)
    descripcion = models.TextField()
    usuario = models.ForeignKey(User)

    class Meta:
        verbose_name_plural = 'Actividades'

    def __str__(self):
        return str(self.id)
