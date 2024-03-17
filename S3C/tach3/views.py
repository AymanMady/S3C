import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.http import HttpResponse

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
        
        # Close the connection
        server.quit()
        
        return HttpResponse("Emails sent successfully.")
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}", status=500)

def verification_Email(request):
    subject = "Test"
    message = f"test emails"
    recipients = ["22086@supnum.mr", "22086@supnum.mr", "aliysidahmedwedad@gmail.com","22018@supnum.mr"]
    
    return send_email(subject, message, recipients)
