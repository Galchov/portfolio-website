from django.conf import settings
from django.shortcuts import render

from django.core.mail import send_mail


def home(request):
    if request.method == 'POST':

        # Get form data
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        # Compose email
        subject = f'New contact form submission from {name}'
        email_message = f'Sender: {name}\nEmail: {email}\nMessage: {message}'
        recipient_list = [settings.DEFAULT_FROM_EMAIL]

        # Send email
        send_mail(
            subject=subject,
            message=email_message,
            from_email=email,
            recipient_list=recipient_list,
            fail_silently=False,
        )

        # Go to page after success
        return render(request, 'home.html')

    return render(request, 'home.html')
