from django.db import models

class Saisie(models.Model):
    route = models.CharField(max_length=200)
    logiciel = models.CharField(max_length=200)
    dtstart = models.DateTimeField()
    duree = models.IntegerField()
    cdret = models.IntegerField()
    mois = models.CharField(max_length=200)