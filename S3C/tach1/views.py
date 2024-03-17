from django.http import HttpResponseNotFound,HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.conf import settings
from main.models import *
from main.models import administrater as Admin
# Create your views here.
import openpyxl

from django.core.mail import send_mail
from random import randint


def home_admin(request):
    return render(request,"home_admin.html")



# _________________________________ETUDIANTS_____________________________________________________________________




def creation_etudiant(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        specialite = request.POST.get('specialite')
        niveau = request.POST.get('niveau')
        compte_existe = Etudiant.objects.filter(email=email)
        if not compte_existe.exists(): 
            etudiant = Etudiant.objects.create(
            nom=nom,
            prénom=prenom,
            email=email,
            spécialité=specialite,
            niveau=niveau
            )
            return redirect('liste_etudiants')
        messages.error(request, "Le compte déja existe")
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



def creation_jury(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        compte_existe = Jery.objects.filter(email=email)
        if not compte_existe.exists(): 
            jery = Jery.objects.create(
            nom=nom,
            prénom=prenom,
            email=email
            )
            return redirect('liste_jury')
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


def creation_admin(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        compte_existe = administrater.objects.filter(email=email)
        if not compte_existe.exists(): 
            admin = administrater.objects.create(
            nom=nom,
            prenom=prenom,
            email=email
            )
            return redirect('liste_admin')
        messages.error(request, "Le compte déja existe")
        return redirect('creation_admin')
    return render(request, "admin/creation_admin.html")



def liste_admin(request):
    admins = administrater.objects.all()
    return render(request, 'admin/liste_admin.html', {'admins': admins})


def supprimer_admin(request, id_admin):
    try:
        admin = administrater.objects.get(pk=id_admin)
        admin.delete()
        return redirect('liste_admin')
    except administrater.DoesNotExist:
        return HttpResponseNotFound("L'admin que vous essayez de supprimer n'existe pas.")
    
    
    
    
def modifier_admin(request, id_admin):
    try:
        admin = administrater.objects.get(pk=id_admin)
        if request.method == 'POST':
            admin.nom = request.POST.get('nom')
            admin.prenom = request.POST.get('prénom')
            admin.email = request.POST.get('email')
            admin.save()
            return redirect('liste_admin')
        return render(request,"admin/modifier_admin.html",{'admin':admin})
    except administrater.DoesNotExist:
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


def travail(request):
    objs=Soumission.objects.all()
    return render(request,'travails_etudiant.html', {"objs":objs})
