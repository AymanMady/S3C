from django.shortcuts import render,HttpResponse
from main.models import *
# Create your views here.

def creation_user(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        motdepasse = request.POST.get('motdepasse')
        role = request.POST.get('role')
        specialite = request.POST.get('specialite')
        niveau = request.POST.get('niveau')
        utilisateur = Utilisateur.objects.create(
            nom=nom,
            prénom=prenom,
            email=email,
            motDePasse=motdepasse,
            role=role,
            spécialité=specialite,
            niveau=niveau
        )
        return HttpResponse("insere")
    return render(request, "creation_user.html")