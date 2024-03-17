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
