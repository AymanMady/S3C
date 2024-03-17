from django.db import models

# Create your models here.
class Défi(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    nom_file = models.CharField(max_length=255)
    chemin_file = models.CharField(max_length=255)
    date_debut = models.DateField()
    date_fin = models.DateField()
