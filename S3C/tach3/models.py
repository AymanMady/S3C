from django.db import models

# Create your models here.
class Défi(models.Model):
    titre = models.CharField(max_length=255)
    desc = models.TextField()
    file = models.FileField(upload_to='uploads/', null=True, blank=True)
    date_debut = models.DateField()
    date_fin = models.DateField()
