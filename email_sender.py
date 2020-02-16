import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import settings

def send_the_mail(name, date, type_leave):
    message = Mail(
        from_email=str(settings.get_from_email()),
        
        to_emails=str(settings.get_to_email()),
        
        subject='Leave Application from %s' % name,
        html_content='Hey <br> %s has applied for a %s leave on %s  Note: THIS IS A TEST FROM MATTERMOST, PLEASE IGNORE THIS EMAIL - Pranoy & Naeem'  % (name, type_leave, date))
    print(settings.get_from_email(),settings.get_to_email(),settings.get_api_key())
    try:
        sg = SendGridAPIClient(
            settings.get_api_key())
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
        
    except Exception as e:
        print(str(e))
