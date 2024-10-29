from django.conf import settings
from django.shortcuts import render

from django.core.mail import send_mail

from .models import Skill


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

    key_skills = Skill.objects.filter(is_key_skill=True)
    tech_skills = Skill.objects.filter(is_key_skill=False)

    context = {
        'key_skills': key_skills,
        'tech_skills': tech_skills,
    }

    return render(request, 'home.html', context)
