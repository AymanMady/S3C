from django.shortcuts import render, redirect, HttpResponse
import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.http import HttpResponse
from main.models import Défi
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages




def create_defi(request):
    if request.method == 'POST':
        titre = request.POST.get('titre')
        desc = request.POST.get('desc')
        file = request.FILES.get('file')  # Utilisez request.FILES pour récupérer les fichiers téléchargés
        date_debut = request.POST.get('date_debut')
        date_fin = request.POST.get('date_fin')

        defi = Défi.objects.create(
            titre=titre,
            desc=desc,
            file=file,
            date_debut=date_debut,
            date_fin=date_fin
        )
        notification_checked = request.POST.get('notification')  # Check if the checkbox is checked
        recipients = ["22086@supnum.mr", "22086@supnum.mr", "aliysidahmedwedad@gmail.com", "22018@supnum.mr"]

        if notification_checked == 'on':  # If the checkbox is checked
            # Send the notification email
            verification_Email(defi)

            # return HttpResponse("Notification email sent.")
            messages.success(request, 'Défi crée avec succès.')
        messages.success(request, 'Défi crée avec succès.')
        return redirect("get_all_defis")
        
    return render(request,'create_defi.html',{'mess':""})

def get_all_defis(request):
    objs=Défi.objects.all()
    return render(request,'defis.html', {"objs":objs})

def get_defi_by_id(defi_id):
    return get_object_or_404(Défi, pk=defi_id)

def update_defi(request,defi_id):
    defi = get_object_or_404(Défi, pk=defi_id)
    if request.method=="POST":
        titre=request.POST.get('titre')
        nom_file=request.POST.get('nom_file')
        description=request.POST.get('description')
        chemin_file=request.POST.get('chemin_file')
        date_debut=request.POST.get('date_debut')
        date_fin=request.POST.get('date_fin')
        if titre:
            defi.titre = titre
        if description:
            defi.description = description
        if nom_file:
            defi.nom_file = nom_file
        if chemin_file:
            defi.chemin_file = chemin_file
        if date_debut:
            defi.date_debut = date_debut
        if date_fin:
            defi.date_fin = date_fin
        defi.save()
        return redirect(get_all_defis)
    return render(request,'update_defi.html',{"obj":defi})

# Delete operation
def delete_defi(request,id):
    defi = get_object_or_404(Défi, pk=id)
    defi.delete()
    return redirect(get_all_defis)

def send_email(subject, message):
    recipients=[]
    usere=Utilisateur.objects.all()
    for i in usere:
        if i.role=="Étudiant":
            recipients.append(i.email)
    source = "s3c.404@gmail.com"
    password = 'wsaw jdjj yrsw pfqv'  
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(source, password)
        
        for recipient in recipients:
            msg = MIMEMultipart()
            msg['From'] = source
            msg['To'] = recipient
            msg['Subject'] = subject
            
            # Add message body
            msg.attach(MIMEText(message, 'plain'))
            
            # Send email
            server.sendmail(source, recipient, msg.as_string())
        
        server.quit()
        
        return HttpResponse("Emails sent successfully.")
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}", status=500)

# def verification_Email(request):
#     subject = "Test"
#     message = f"test emails"
#     recipients = ["22086@supnum.mr", "22086@supnum.mr", "aliysidahmedwedad@gmail.com","22018@supnum.mr"]
    
#     return send_email(subject, message, recipients)

from datetime import datetime

def verification_Email(defi):

    now = datetime.now()
    subject = "S3C"
    message = f" defi : {defi.titre} \n descrition : {defi.desc} \n de {defi.date_debut} a {defi.date_fin}"
    recipients = ["22086@supnum.mr", "aliysidahmedwedad@gmail.com"]
    # defis_to_verify = Défi.objects.filter(date_debut__lte=now)
    # for defi in defis_to_verify:
    send_email(subject, message)
    return HttpResponse("Verification emails sent.")  # Optional response
# verification_Email()

# def verification_Email(request):
#     subject = "Test"
#     message = f"test emails"
#     recipients = ["22086@supnum.mr", "22086@supnum.mr", "aliysidahmedwedad@gmail.com","22018@supnum.mr"]
    
#     return send_email(subject, message, recipients)



# def upload_file(request):
#     if request.method == 'POST':
#         form = FileUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             new_file = form.save()
#             return redirect('file_list')
#     else:
#         form = FileUploadForm()
#     return render(request, 'upload_file.html', {'form': form})

# def file_list(request):
#     files = UploadedFile.objects.all()  
#     return render(request, 'file_list.html', {'files': files})

def download_or_view_file(request, file_id):
    file = Défi.objects.get(pk=file_id)
    if file.file.name.endswith('.pdf'):

        with open(file.file.path, 'rb') as pdf_file:
            response = HttpResponse(pdf_file.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'inline; filename="{file.file.name}"'
            return response
    else:
        # Pour tous les autres types de fichiers, forcez le téléchargement
        with open(file.file.path, 'rb') as file_content:
            response = HttpResponse(file_content.read())
            response['Content-Disposition'] = f'attachment; filename="{file.file.name}"'
            return response
