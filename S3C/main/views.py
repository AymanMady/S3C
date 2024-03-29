from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Utilisateur, Équipe, Inscription, Etudiant
from django.db.models import Count
from django.shortcuts import render
from django.db.models import Q
from django.contrib import messages

from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ObjectDoesNotExist

from django.core.mail import send_mail
from random import randint
from django.contrib import messages
from django.conf import settings
from .forms import *

from .forms import  InscriptionJuryForm
from django.db.models import Q



def inscription_jury(request):
    if request.method == 'POST':
        form = InscriptionJuryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login.html')  # Rediriger vers le tableau de bord après l'inscription
    else:
        form = InscriptionJuryForm()  # Utilisation de InscriptionJuryForm() pour instancier le formulaire
    return render(request, 'inscription_jury.html', {'form': form})



def inscription_etudiant(request):
    if request.method == 'POST':
        form = EtudiantForm(request.POST)
        if form.is_valid():
            # Si le formulaire est valide, enregistrez l'étudiant
            form.save()
            # Redirigez l'utilisateur vers une page de confirmation ou toute autre page souhaitée
            return redirect('login')
    else:
        # Si la méthode de la requête n'est pas POST, initialisez simplement le formulaire
        form = EtudiantForm()
    return render(request, 'inscription_etudiant.html', {'form': form})


def traiter_inscription(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # Faites ce que vous avez besoin de faire avec l'email, comme vérifier s'il existe déjà dans votre base de données
        # Par exemple, vous pouvez effectuer une vérification d'email en temps réel ici et renvoyer un message JSON approprié
        if email:
            # Traitez l'email ici (vérification, enregistrement en base de données, etc.)
            # Par exemple, vous pouvez vérifier si l'email est déjà enregistré dans votre base de données
            if email_existe_deja(email):
                return JsonResponse({'message': 'L\'email existe déjà'})
            else:
                return JsonResponse({'message': 'L\'email est valide'})
        else:
            return JsonResponse({'message': 'L\'email est requis'})

    return JsonResponse({'message': 'Méthode non autorisée'})


# La fonction de vue ajustée
def verifier_email(request):
    if request.method == "GET" and 'email' in request.GET:
        email = request.GET.get('email')
        if Utilisateur.objects.filter(email=email).exists():
            return JsonResponse({'message': 'Utilisateur existe'})
        elif Etudiant.objects.filter(email=email).exists():
            return JsonResponse({'message': 'Étudiant'})
        elif Jery.objects.filter(email=email).exists():
            return JsonResponse({'message': 'Jury'})
        else:
            return JsonResponse({'message': 'Non trouvé'})
    else:
        # Lors d'une requête GET sans paramètre email, afficher le formulaire
        return render(request, 'verifier_email.html')




def generate_verification_code():
    return str(randint(100000, 999999))

def logout_user(request):
    logout(request)
    return redirect('acceuil_principale')


def send_verification_email(to_email, verification_code):
    subject = 'Verification Code'
    message = f'Your verification code is: {verification_code}'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [to_email]
    send_mail(subject, message, from_email, recipient_list)

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

def acceuil_principale(request):
    return render(request,"acceuil_principale.html") 

def etudient_view(request):
    return redirect("home_etud")
def admin_view(request):
    return redirect("home_admin")
def jery_view(request):
    return redirect("home_jery")


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

def forgetPasword(request):

    if request.method == "POST":
        email = request.POST.get('email')
        try:
            user = Utilisateur.objects.filter(email=email).first()
        except ObjectDoesNotExist:
            return render(request, 'login.html', {"mess": "Utilisateur n'existe pas !"})
        if user:
            code = generate_verification_code()
            send_verification_email(email, code)
            request.session['verification_code_'] = code
            request.session['mail_'] = email
            return render(request,"verification_code.html")
            return HttpResponse(code)
    return render(request, 'forgot-password.html', {"mess": ""})

def verification_code(request):
    if request.method == "POST":
        code = request.POST.get('code')
        if code:
            # Check if the code matches the one stored in the session
            stored_code = request.session.get('verification_code_')
            if stored_code == code:
                return render(request, "change_password.html",{'mess':""})
            else:
                # Code is invalid, inform the user
                return render(request, "verification_code.html",{'mess':"code incorrect"})
        else:
            # Code is not provided in the request
            return render(request, "verification_code.html",{'mess':"code incorrect"})  # Or handle it as you wish
    else:
        # The view should only handle POST requests
        return render(request,"verification_code.html",{'mess':""})  
    
def change_mot(request):
    if request.method == "POST":
        mot1 = request.POST.get('mot1')
        mot2 = request.POST.get('mot2')
        mail=request.session.get('mail_')
        user = Utilisateur.objects.filter(email=mail).first()
        if mot1 == mot2:
            if user:
                user.motDePasse=mot1
                user.save()
                return redirect(login)
            
        else:
            return render(request, "change_password.html",{'mess':"les mots de passe ne sont pas identique  "})



