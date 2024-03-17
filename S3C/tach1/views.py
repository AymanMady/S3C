from django.http import HttpResponseNotFound,HttpResponse
from django.shortcuts import render,redirect
from random import randint
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from main.models import *
# Create your views here.
import openpyxl



def generate_verification_code():
    return str(randint(100000, 999999))



def send_verification_email(to_email, verification_code):
    subject = 'Verification Code'
    message = f'Your verification code is: {verification_code}'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [to_email]
    send_mail(subject, message, from_email, recipient_list)




# _________________________________ETUDIANTS_____________________________________________________________________

def verification_etudiant(request):
    email = request.session.get('email')
    verification_code = request.session.get('verification_code')
    if not email or not verification_code:
        messages.error(request, 'Données de session de vérification invalides.')
        return redirect('creation_etudiant')
    if request.method == 'POST':
        entered_code = request.POST.get('code')
        if entered_code == verification_code:
            nom = request.session.get('nom')
            prenom = request.session.get('prenom')
            specialite = request.session.get('specialite')
            niveau = request.session.get('niveau')
            etudiant = Etudiant.objects.create(
            nom=nom,
            prénom=prenom,
            email=email,
            spécialité=specialite,
            niveau=niveau
            )
            return redirect('creation_etudiant')
        else:
            messages.error(request, 'Code de vérification invalide.')
    return render(request, 'etudiants/verification_etudiant.html', {'email': email, 'verification_code': verification_code})



def creation_etudiant(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        specialite = request.POST.get('specialite')
        niveau = request.POST.get('niveau')
        nom = request.session.get('nom')
        prenom = request.session.get('prenom')
        specialite = request.session.get('specialite')
        niveau = request.session.get('niveau')
        etudiant = Etudiant.objects.create(
        nom=nom,
        prénom=prenom,
        email=email,
        spécialité=specialite,
        niveau=niveau
        )

        return redirect('creation_etudiant')
    return render(request, "etudiants/creation_etudiant.html")


def liste_etudiants(request):
    etudiants = Etudiant.objects.all()
    return render(request, 'etudiants/liste_etudiants.html', {'etudiants': etudiants})

def supprimer_etudiant(request, id_etudiant):
    try:
        etudiant = Etudiant.objects.get(pk=id_etudiant)
        etudiant.delete()
        return redirect('liste_etudiants')
    except Etudiant.DoesNotExist:
        return HttpResponseNotFound("L'étudiant que vous essayez de supprimer n'existe pas.")
    
    
    
def modifier_etudiant(request, id_etudiant):
    try:
        etudiant = Etudiant.objects.get(pk=id_etudiant)
        if request.method == 'POST':
            etudiant.nom = request.POST.get('nom')
            etudiant.prénom = request.POST.get('prenom')
            etudiant.spécialité = request.POST.get('specialite')
            etudiant.niveau = request.POST.get('niveau')
            etudiant.save()
            return redirect('liste_etudiants')
        return render(request,"etudiants/modifier_etudiant.html",{'etudiant':etudiant})
    except Etudiant.DoesNotExist:
        return HttpResponseNotFound("L'étudiant que vous essayez de modifier n'existe pas.")
    
    
# _________________________________FIN ETUDIANTS_____________________________________________________________________



# _________________________________JURY______________________________________________________________


def verification_jury(request):
    email = request.session.get('email')
    verification_code = request.session.get('verification_code')
    if not email or not verification_code:
        messages.error(request, 'Données de session de vérification invalides.')
        return redirect('creation_jury')
    if request.method == 'POST':
        entered_code = request.POST.get('code')
        if entered_code == verification_code:
            nom = request.session.get('nom')
            prenom = request.session.get('prenom')
            jury = Jery.objects.create(
            nom=nom,
            prénom=prenom,
            email=email
            )
            return redirect('creation_jury')
        else:
            messages.error(request, 'Code de vérification invalide.')
    return render(request, 'jury/verification_jury.html', {'email': email, 'verification_code': verification_code})




def creation_jury(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        compte_existe = Jery.objects.filter(email=email)
        if not compte_existe.exists(): 
            code = generate_verification_code()
            send_verification_email(email, code)
            request.session['verification_code'] = code
            request.session['nom'] = nom
            request.session['prenom'] = prenom
            request.session['email'] = email
            return redirect('verification_jury')
        messages.error(request, "Le compte déja existe")
        return redirect('creation_jury')
    return render(request, "jury/creation_jury.html")



def liste_jury(request):
    jurys = Jery.objects.all()
    return render(request, 'jury/liste_jury.html', {'jurys': jurys})


def supprimer_jury(request, id_jury):
    try:
        jury = Jery.objects.get(pk=id_jury)
        jury.delete()
        return redirect('liste_jury')
    except Jery.DoesNotExist:
        return HttpResponseNotFound("Le jury que vous essayez de supprimer n'existe pas.")
    
    
    
    
def modifier_jury(request, id_jury):
    try:
        jury = Jery.objects.get(pk=id_jury)
        if request.method == 'POST':
            jury.nom = request.POST.get('nom')
            jury.prénom = request.POST.get('prenom')
            jury.save()
            return redirect('liste_jury')
        return render(request,"jury/modifier_jury.html",{'jury':jury})
    except Jery.DoesNotExist:
        return HttpResponseNotFound("Le jury que vous essayez de modifier n'existe pas.")
    
# _________________________________END JURY______________________________________________________________


# _____________________________________ADMIN__________________________________________________________


def verification_admin(request):
    email = request.session.get('email')
    verification_code = request.session.get('verification_code')
    if not email or not verification_code:
        messages.error(request, 'Données de session de vérification invalides.')
        return redirect('creation_admin')
    if request.method == 'POST':
        entered_code = request.POST.get('code')
        if entered_code == verification_code:
            nom = request.session.get('nom')
            prenom = request.session.get('prenom')
            admin = Admin.objects.create(
            nom=nom,
            prénom=prenom,
            email=email
            )
            return redirect('creation_admin')
        else:
            messages.error(request, 'Code de vérification invalide.')
    return render(request, 'admin/verification_admin.html', {'email': email, 'verification_code': verification_code})




def creation_admin(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        compte_existe = Admin.objects.filter(email=email)
        if not compte_existe.exists(): 
            code = generate_verification_code()
            send_verification_email(email, code)
            request.session['verification_code'] = code
            request.session['nom'] = nom
            request.session['prenom'] = prenom
            request.session['email'] = email
            return redirect('verification_admin')
        messages.error(request, "Le compte déja existe")
        return redirect('creation_admin')
    return render(request, "admin/creation_admin.html")



def liste_admin(request):
    admins = Admin.objects.all()
    return render(request, 'admin/liste_admin.html', {'admins': admins})


def supprimer_admin(request, id_admin):
    try:
        admin = Admin.objects.get(pk=id_admin)
        admin.delete()
        return redirect('liste_admin')
    except Admin.DoesNotExist:
        return HttpResponseNotFound("L'admin que vous essayez de supprimer n'existe pas.")
    
    
    
    
def modifier_admin(request, id_admin):
    try:
        admin = Admin.objects.get(pk=id_admin)
        if request.method == 'POST':
            admin.nom = request.POST.get('nom')
            admin.prénom = request.POST.get('prenom')
            admin.save()
            return redirect('liste_admin')
        return render(request,"admin/modifier_admin.html",{'admin':admin})
    except Admin.DoesNotExist:
        return HttpResponseNotFound("L'admin que vous essayez de modifier n'existe pas.")
    
# _________________________________END ADMIN______________________________________________________________
def import_etudiantsl(request):
    if request.method == "POST" and request.FILES.get('excel_file'):
        excel_file = request.FILES['excel_file']
        wb = openpyxl.load_workbook(excel_file)
        emails = Etudiant.objects.values_list('email', flat=True)

        sheet = wb.active

        for row in sheet.iter_rows(min_row=2, values_only=True):
            if row[2] not in emails  :
                obj = Etudiant(nom=row[0], prénom=row[1],  email=row[2], spécialité=row[3], niveau=row[4])  # Adjust field names accordingly
                obj.save()

        print('Data imported successfully')
        return render(request, "import_etudiant.html")
    return render(request, "import_etudiant.html")