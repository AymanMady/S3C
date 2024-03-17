from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Utilisateur)
admin.site.register(Équipe)
admin.site.register(Inscription)
admin.site.register(Défi)
admin.site.register(Soumission)
admin.site.register(Évaluation)
admin.site.register(Résultat)