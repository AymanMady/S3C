from django.shortcuts import render,HttpResponse
from main.models import *
import openpyxl ,os
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
