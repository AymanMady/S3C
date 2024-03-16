from django.shortcuts import render, redirect
from .models import Équipe, Utilisateur, Inscription
from django.core.exceptions import ValidationError

def creer_equipe(request):
    if request.method == 'POST':
        # Exemple de récupération des données du formulaire
        nom_equipe = request.POST.get('nom_equipe')
        lead_id = request.POST.get('lead_id')
        adjoint_id = request.POST.get('adjoint_id')
        membres_ids = request.POST.getlist('membres_ids')  # Supposant que c'est une liste d'IDs

        # Validez ici les contraintes spécifiques à votre logique métier

        try:
            equipe = Équipe(nomEquipe=nom_equipe, leadID_id=lead_id, adjointID_id=adjoint_id)
            equipe.full_clean()  # Valide les contraintes du modèle
            
            # Ici, ajoutez votre logique de validation spécifique
            # Assurez-vous que tous les critères sont respectés

            equipe.save()

            # Après avoir sauvegardé l'équipe, vous pouvez ajouter les membres
            for membre_id in membres_ids:
                Inscription(utilisateur_id=membre_id, équipe=equipe).save()

            return redirect('some-view-name')  # Redirigez vers une vue de succès ou la liste des équipes
        except ValidationError as e:
            # Gérez l'erreur ou retournez-la au formulaire
            pass

    # GET request ou après échec de validation
    return render(request, 'nom_du_template.html', context)
