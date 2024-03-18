from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Utilisateur, Équipe, Inscription, Etudiant
from django.db.models import Count
from django.shortcuts import render
from .models import Équipe
from django.db.models import Q
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ObjectDoesNotExist


def creer_equipe(request):
    if request.method == 'POST':
        nom_equipe = request.POST.get('nom_equipe')
        lead_id = request.POST.get('lead_id')
        adjoint_id = request.POST.get('adjoint_id')
        membres_ids = request.POST.getlist('membres_ids')
        
        # Vérification que tous les membres sont des étudiants
        
        lead = Utilisateur.objects.get(pk=lead_id)
        lead_etud = Etudiant.objects.get(email=lead.email)
        adjoint = Utilisateur.objects.get(pk=adjoint_id)
        adjoint_etu = Etudiant.objects.get(email=adjoint.email)
        filieres_a_verifier = ['CNM', 'DSI', 'RSS']
        compteur_filieres = {filiere: 0 for filiere in filieres_a_verifier}
        count_l2_students = 0
        for membre_id in membres_ids:
            user = Utilisateur.objects.get(pk=membre_id)
            etudiant = Etudiant.objects.get(email=user.email)
            if etudiant.niveau == 'L2':
                  count_l2_students += 1
          
            compteur_filieres[etudiant.spécialité] += 1
        
        toutes_les_filieres_presentes = all(compteur_filieres[filiere] > 0 for filiere in filieres_a_verifier)

        if not toutes_les_filieres_presentes:
            return HttpResponse("Il manque au moins un étudiant pour une ou plusieurs filières.")
      
        if lead_etud.niveau == adjoint_etu.niveau:
            return HttpResponse("Le lead et l'adjoint doivent avoir des niveaux d'études différents.")
        if count_l2_students < 4:
            return HttpResponse("Il doit y avoir au moins 4 étudiants de niveau L2 dans l'équipe.")
        if len(membres_ids) < 6 or len(membres_ids) > 8:
            return HttpResponse("Le nombre de membres doit être entre 6 et 8.")
        
        equipe = Équipe(nomEquipe=nom_equipe, leadID=lead, adjointID=adjoint, nombreMembres=len(membres_ids))
        equipe.save()
        for membre_id in membres_ids:
            Inscription(utilisateur_id=membre_id, équipe=equipe, role='membre').save()
            
        return redirect('success_url')  
    utilisateurs = Utilisateur.objects.filter(role='étudiant').annotate(num_inscriptions=Count('inscription')).filter(num_inscriptions=0)
    return render(request, 'creer_equipe.html', {'utilisateurs': utilisateurs})

def liste_equipes(request):
    equipes = Équipe.objects.all().select_related('leadID', 'adjointID')
    return render(request, 'liste_equipes.html', {'equipes': equipes})

def detail_equipe(request, equipe_id):
    equipe = get_object_or_404(Équipe, pk=equipe_id)
    inscriptions = Inscription.objects.filter(équipe=equipe)
    membres = [inscription.utilisateur for inscription in inscriptions]
    return render(request, 'detail_equipe.html', {'equipe': equipe, 'membres': membres})

def etudient_view(request):
    return HttpResponse("je suis un etudiant")
def admin_view(request):
    return HttpResponse("je suis un admin")
def jery_view(request):
    return HttpResponse("je suis un jery")


def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        pwd = request.POST.get('password')
        try:
            user = Utilisateur.objects.filter(email=email).first()
        except ObjectDoesNotExist:
            return render(request, 'login.html', {"mess": "Utilisateur n'existe pas !"})
        if user:
            if  user.motDePasse ==pwd :
                if user.role.lower() == "étudiant":
                    return redirect('etudient_view')  # Assuming 'etudient_view' is a URL name
                elif user.role.lower() == "organisateur":
                    return redirect('admin_view')  # Assuming 'admin_view' is a URL name
                else:
                    return redirect('jery_view')  # Assuming 'jery_view' is a URL name
            else:
                return render(request, 'login.html', {"mess": "Mot de passe incorrect !"})
        else:
            return render(request, 'login.html', {"mess": "Utilisateur n'existe pas !"})

    return render(request, 'login.html', {"mess": ""})

