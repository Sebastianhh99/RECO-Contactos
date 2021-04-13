from django.db import models
from django.db.models.fields import related

# Create your models here.

class Pleasure(models.Model):
    pleasure=models.CharField(max_length=250)

class Relationship(models.Model):
    relation=models.CharField(max_length=250)


class Person(models.Model):
    class Meta:
        verbose_name="Persona"
        verbose_name_plural="Personas"

    name=models.CharField(max_length=250)
    city=models.CharField(max_length=250)
    country=models.CharField(max_length=250)
    phone=models.IntegerField()
    birthday=models.DateField()
    relation=models.ForeignKey(Relationship,on_delete=models.CASCADE)
    pleasure=models.ForeignKey(Pleasure,on_delete=models.CASCADE)
