from django.conf import settings
from django.shortcuts import render, redirect
from django.core.mail import send_mail

from .models import Skill
from .forms import ContactForm


def home(request):
    context = {}
    form = ContactForm(request.POST or None)
    email_sent = False
    sender_name = ''

    if request.method == 'POST':
        if form.is_valid():

            # Get form data
            sender_name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Compose email
            subject = f'New contact form submission from {sender_name}'
            email_message = f'Sender: {sender_name}\nEmail: {email}\nMessage: {message}'
            recipient_list = [settings.DEFAULT_FROM_EMAIL]

            # Send email
            send_mail(
                subject=subject,
                message=email_message,
                from_email=email,
                recipient_list=recipient_list,
                fail_silently=False,
            )

            email_sent = True
            form = ContactForm()

    key_skills = Skill.objects.filter(is_key_skill=True)
    tech_skills = Skill.objects.filter(is_key_skill=False)

    context.update({
        'form': form,
        'sender_name': sender_name,
        'email_sent': email_sent,
        'key_skills': key_skills,
        'tech_skills': tech_skills,
    })

    return render(request, 'home.html', context)
