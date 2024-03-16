from django.db import models

class Utilisateur(models.Model):
    ROLES_CHOICES = (
        ('étudiant', 'Étudiant'),
        ('organisateur', 'Organisateur'),
        ('jury', 'Jury'),
    )
    NIVEAU_CHOICES = (
        ('L1', 'L1'),
        ('L2', 'L2'),
        ('L3', 'L3'),
        ('M1', 'M1'),
        ('M2', 'M2'),
    )
    nom = models.CharField(max_length=255)
    prénom = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    motDePasse = models.CharField(max_length=255)
    role = models.CharField(max_length=12, choices=ROLES_CHOICES)
    spécialité = models.CharField(max_length=255)
    niveau = models.CharField(max_length=3, choices=NIVEAU_CHOICES)