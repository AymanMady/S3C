from django.shortcuts import render , redirect
from main.models import *
# Create your views here.

def home_etud(request):
    return render(request,"home_etud.html")

def cree_groupe(request):
    return render(request,"cree_groupe.html")

def render_travail(request):
    all_defi = Défi.objects.all()
    all_equipe = Équipe.objects.all()

    if request.method == 'POST':
        # Récupérer les données du formulaire
        équipe_id = request.POST.get('équipe')
        défi_id = request.POST.get('défi')
        file = request.FILES.get('file')
        lien_git = request.POST.get('lienGit')
        date_soumission = request.POST.get('dateSoumission')

        # Créer la soumission avec les données reçues
        soumission = Soumission.objects.create(
            équipe_id=équipe_id,
            défi_id=défi_id,
            file=file,
            lienGit=lien_git,
            dateSoumission=date_soumission,
        )
        
        return redirect('home') 
    else:
        return render(request, 'rendre.html',{'défis':all_defi,'equipes':all_equipe})

