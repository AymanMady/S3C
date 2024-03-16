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

class Équipe(models.Model):
    nomEquipe = models.CharField(max_length=255)
    leadID = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='lead_teams')
    adjointID = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='adjoint_teams')
    nombreMembres = models.IntegerField()

class Inscription(models.Model):
    ROLE_CHOICES = (
        ('lead', 'Lead'),
        ('adjoint', 'Adjoint'),
        ('membre', 'Membre'),
    )
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    équipe = models.ForeignKey(Équipe, on_delete=models.CASCADE)
    role = models.CharField(max_length=7, choices=ROLE_CHOICES)

class Défi(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    nom_file = models.CharField(max_length=255)
    chemin_file = models.CharField(max_length=255)
    date_debut = models.DateField()
    date_fin = models.DateField()

class Soumission(models.Model):
    STATUS_CHOICES = (
        ('soumis', 'Soumis'),
        ('évalué', 'Évalué'),
    )
    équipe = models.ForeignKey(Équipe, on_delete=models.CASCADE)
    défi = models.ForeignKey(Défi, on_delete=models.CASCADE)
    lienGit = models.CharField(max_length=255)
    dateSoumission = models.DateTimeField()
    status = models.CharField(max_length=7, choices=STATUS_CHOICES)

class Évaluation(models.Model):
    soumission = models.ForeignKey(Soumission, on_delete=models.CASCADE)
    score = models.IntegerField()
    commentaires = models.TextField()

class Résultat(models.Model):
    équipe = models.ForeignKey(Équipe, on_delete=models.CASCADE)
    scoreTotal = models.IntegerField()