from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Utilisateur, Équipe, Inscription, Etudiant
from django.db.models import Count
from django.shortcuts import render
from django.db.models import Q
from django.contrib import messages

# def creer_equipe(request):
#     if request.method == 'POST':
#         nom_equipe = request.POST.get('nom_equipe')
#         lead_id = request.POST.get('lead_id')
#         adjoint_id = request.POST.get('adjoint_id')
#         membres_ids = request.POST.getlist('membres_ids')
        
#         # Vérification que tous les membres sont des étudiants
        
#         lead = Utilisateur.objects.get(pk=lead_id)
#         lead_etud = Etudiant.objects.get(email=lead.email)
#         adjoint = Utilisateur.objects.get(pk=adjoint_id)
#         adjoint_etu = Etudiant.objects.get(email=adjoint.email)
#         filieres_a_verifier = ['CNM', 'DSI', 'RSS']
#         compteur_filieres = {filiere: 0 for filiere in filieres_a_verifier}
#         count_l2_students = 0
#         for membre_id in membres_ids:
#             user = Utilisateur.objects.get(pk=membre_id)
#             etudiant = Etudiant.objects.get(email=user.email)
#             if etudiant.niveau == 'L2':
#                   count_l2_students += 1
          
#             compteur_filieres[etudiant.spécialité] += 1
        
#         toutes_les_filieres_presentes = all(compteur_filieres[filiere] > 0 for filiere in filieres_a_verifier)
#         utilisateurs = Utilisateur.objects.filter(role='étudiant').annotate(num_inscriptions=Count('inscription')).filter(num_inscriptions=0)
#         if not toutes_les_filieres_presentes:
#             # return HttpResponse("Il manque au moins un étudiant pour une ou plusieurs filières.")
#             messages.success(request, 'Il manque au moins un étudiant pour une ou plusieurs filières.')
#             return render(request, 'creer_equipe.html', {'utilisateurs': utilisateurs})
      
#         if lead_etud.niveau == adjoint_etu.niveau:
#             # return HttpResponse("Le lead et l'adjoint doivent avoir des niveaux d'études différents.")
#             messages.success(request, "Le lead et l'adjoint doivent avoir des niveaux d'études différents.")
#             return render(request, 'creer_equipe.html', {'utilisateurs': utilisateurs})
#         if count_l2_students < 4:
#             return HttpResponse("Il doit y avoir au moins 4 étudiants de niveau L2 dans l'équipe.")
#         if len(membres_ids) < 6 or len(membres_ids) > 8:
#             return HttpResponse("Le nombre de membres doit être entre 6 et 8.")
        
#         equipe = Équipe(nomEquipe=nom_equipe, leadID=lead, adjointID=adjoint, nombreMembres=len(membres_ids))
#         equipe.save()
#         for membre_id in membres_ids:
#             Inscription(utilisateur_id=membre_id, équipe=equipe, role='membre').save()
            
#         return redirect('liste_equipes')  
#     utilisateurs = Utilisateur.objects.filter(role='étudiant').annotate(num_inscriptions=Count('inscription')).filter(num_inscriptions=0)
#     return render(request, 'creer_equipe.html', {'utilisateurs': utilisateurs})



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
        utilisateurs = Utilisateur.objects.filter(role='étudiant').annotate(num_inscriptions=Count('inscription')).filter(num_inscriptions=0)
        
        if not toutes_les_filieres_presentes:
            messages.error(request, 'Il manque au moins un étudiant pour une ou plusieurs filières.')
            return render(request, 'creer_equipe.html', {'utilisateurs': utilisateurs})
      
        if lead_etud.niveau == adjoint_etu.niveau:
            messages.error(request, "Le lead et l'adjoint doivent avoir des niveaux d'études différents.")
            return render(request, 'creer_equipe.html', {'utilisateurs': utilisateurs})
        
        if count_l2_students < 4:
            messages.error(request, "Il doit y avoir au moins 4 étudiants de niveau L2 dans l'équipe.")
            return render(request, 'creer_equipe.html', {'utilisateurs': utilisateurs})
        
        if len(membres_ids) < 6 or len(membres_ids) > 8:
            messages.error(request, "Le nombre de membres doit être entre 6 et 8.")
            return render(request, 'creer_equipe.html', {'utilisateurs': utilisateurs})
        
        equipe = Équipe(nomEquipe=nom_equipe, leadID=lead, adjointID=adjoint, nombreMembres=len(membres_ids))
        equipe.save()
        
        for membre_id in membres_ids:
            Inscription(utilisateur_id=membre_id, équipe=equipe, role='membre').save()
            
        messages.success(request, "L'équipe a été créée avec succès.")
        return redirect('liste_equipes')  
    
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
