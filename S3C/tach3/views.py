import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.http import HttpResponse
from main.models import Défi
from django.shortcuts import get_object_or_404,render,redirect


def create_defi(request):
    if request.method=='POST':
        titre=request.POST.get('titre')
        nom_file=request.POST.get('nom_file')
        description=request.POST.get('description')
        chemin_file=request.POST.get('chemin_file')
        date_debut=request.POST.get('date_debut')
        date_fin=request.POST.get('date_fin')
        defi = Défi.objects.create(
            titre=titre,
            description=description,
            nom_file=nom_file,
            chemin_file=chemin_file,
            date_debut=date_debut,
            date_fin=date_fin
        )
        return redirect(get_all_defis)

    return render(request,'create_defi.html',{'mess':""})

# Read operation (Retrieve all records)
def get_all_defis(request):
    objs=Défi.objects.all()
    return render(request,'defis.html',{"objs":objs})

# Read operation (Retrieve a single record by ID)
def get_defi_by_id(defi_id):
    return get_object_or_404(Défi, pk=defi_id)

# Update operation
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

def send_email(subject, message, recipients):
    source = "s3c.404@gmail.com"
    password = 'wsaw jdjj yrsw pfqv'  # Make sure to use your actual email password
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    
    try:
        # Set up the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(source, password)
        
        for recipient in recipients:
            # Create a multipart message
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

def verification_Email():
    now = datetime.now()
    subject = "Test"
    message = f"Test emails"
    recipients = ["22086@supnum.mr", "22086@supnum.mr", "aliysidahmedwedad@gmail.com", "22018@supnum.mr"]
    
    # Assuming date_debut is the DateTimeField in your model
    defis_to_verify = Défi.objects.filter(date_debut__lte=now)
    
    for defi in defis_to_verify:
        send_email(subject, message, recipients)
    
    return HttpResponse("Verification emails sent.")  # Optional response
verification_Email()

def verification_Email(request):
    subject = "Test"
    message = f"test emails"
    recipients = ["22086@supnum.mr", "22086@supnum.mr", "aliysidahmedwedad@gmail.com","22018@supnum.mr"]
    
    return send_email(subject, message, recipients)