from django.shortcuts import render , redirect
from main.models import *
# Create your views here.

def etudiants(request):
    all_etudiants = Etudiant.objects.all()
    return render(request,"etudiant.html",{'etudiants':all_etudiants})

def jerys(request):
    all_jerys = Jery.objects.all()
    return render(request,"jerys.html",{"jerys":all_jerys})

def add_etudiant(request):
    return render(request,"add_etudiant.html")

def add_jerys(request):
    return render(request,"add_jerys.html")

def liste_affectations(request):
    affectations = AffectationJury.objects.all()
    return render(request, 'liste_affectations.html', {'affectations': affectations})

def modifier_affectation(request, id):
    defis=Défi.objects.all()
    jerys=Jery.objects.all()
    affectation = AffectationJury.objects.get(pk=id)
    if request.method == 'POST':
        id_jery = request.POST.get('id_jery')
        id_defi = request.POST.get('id_defi')
        
        # Vérifiez si les identifiants du membre du jury et du défi sont valides
        membre_jury = Jery.objects.filter(id=id_jery).first()
        defi = Défi.objects.filter(id=id_defi).first()

        if membre_jury and defi:
            # Mettez à jour l'affectation avec les nouvelles données
            affectation.membre_jury = membre_jury
            affectation.defi = defi
            affectation.save()
            return redirect('liste_affectations')
        else:
            return render(request, 'modifier_affectation.html', {'affectation': affectation, 'error': 'Membre du jury ou défi invalide'})

    return render(request, 'modifier_affectation.html', {'affectation': affectation,"jerys":jerys,"defis":defis})




def supprimer_affectation(request, id):
    affectation = AffectationJury.objects.get(pk=id)
    affectation.delete()
    return redirect('liste_affectations')




# def noter_equipe(request, equipe_id, critere_id):
#     equipe = Équipe.objects.get(pk=equipe_id)
#     critere = Critère.objects.get(pk=critere_id)

#     if request.method == "POST":
#         note = request.POST.get('note')
#         commentaire = request.POST.get('commentaire')
        
#         # Vérifier si une évaluation existe déjà pour cet équipe et ce critère
#         soumission = Soumission.objects.get(équipe=equipe, défi=critere.defi)
#         existant = Évaluation.objects.filter(soumission=soumission, critere=critere).exists()
        
#         if not existant:
#             # Créer une nouvelle évaluation
#             nouvelle_evaluation = Évaluation.objects.create(
#                 soumission=soumission,
#                 critere=critere,
#                 note=note,
#                 commentaire=commentaire
#             )
#             return redirect("page_de_confirmation")  # Rediriger vers une page de confirmation
#         else:
#             # Une évaluation existe déjà pour cet équipe et ce critère
#             return render(request, "message.html", {"message": "Une évaluation existe déjà pour cet équipe et ce critère."})
    
#     return render(request, "formulaire_evaluation.html", {"equipe": equipe, "critere": critere})


# def calculer_note_moyenne_equipe(equipe):
#     soumissions = Soumission.objects.filter(équipe=equipe)
#     total_notes = 0
#     total_coefficients = 0

#     for soumission in soumissions:
#         evaluations = Évaluation.objects.filter(soumission=soumission)
#         for evaluation in evaluations:
#             grille = GrilleEvaluation.objects.get(defi=soumission.défi, critere=evaluation.critere)
#             total_notes += evaluation.note * grille.coefficient
#             total_coefficients += grille.coefficient

#     if total_coefficients == 0:
#         return 0
#     else:
#         return total_notes / total_coefficients

# def get_defis_et_criteres():
#     defis_criteres = {}

#     # Récupérer tous les défis de la base de données
#     defis = Défi.objects.all()

#     # Boucler sur chaque défi pour récupérer ses critères
#     for defi in defis:
#         criteres = Critère.objects.filter(defi=defi)
#         defis_criteres[defi] = criteres

#     return defis_criteres

# def noter_equipes_pour_defis(request):
#     # Obtenez toutes les équipes de la base de données
#     equipes = Équipe.objects.all()

#     # Pour chaque équipe, calculez le score pour chaque défi
#     scores = {}
#     for equipe in equipes:
#         scores[equipe.nomEquipe] = {}
#         for defi, critere_liste in get_defis_et_criteres():
#             score_total = 0
#             for critere, coefficient in critere_liste:
#                 # Ici, vous pouvez définir la logique pour noter chaque critère pour une équipe donnée
#                 # Par exemple, supposons que vous avez des valeurs de note stockées dans votre modèle Évaluation
#                 note_critere = equipe.evaluer_critere(critere)  # Supposons que vous avez une méthode dans le modèle Équipe pour récupérer la note pour un critère donné
#                 score_total += note_critere * coefficient
#             scores[equipe.nomEquipe][defi] = score_total

#     # Passez les scores calculés au template pour affichage
#     return render(request, 'scores.html', {'scores': scores})



def affectation(request):
    jerys = Jery.objects.all()
    defs = Défi.objects.all()

    if request.method == "POST":
        id_jery = request.POST.get("id_jery")
        id_defi = request.POST.get("id_defi")

        if Jery.objects.filter(id=id_jery).first() and Défi.objects.filter(id=id_defi).first():
            if not AffectationJury.objects.filter(membre_jury_id=id_jery, defi=id_defi).first():
                nouvelle_affectation = AffectationJury.objects.create(membre_jury_id=id_jery, defi_id=id_defi)
                return redirect("liste_affectations")  # Rediriger vers une vue de succès
            else:
                # Affectation déjà existante
                return render(request, "effectation.html", {"jerys": jerys, "defis": defs, "mess": "Affectation déjà existante"})
        else:
            # Membre du jury ou défi inexistant
            return render(request, "effectation.html", {"jerys": jerys, "defis": defs, "mess": "Membre du jury ou défi inexistant"})

    return render(request, "effectation.html", {"jerys": jerys, "defis": defs, "mess": ""})