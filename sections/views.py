from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail

from .models import Skill
from .forms import ContactForm


def home(request):
    context = {}
    form = ContactForm(request.POST or None)
    email_sent = False
    subject = ''

    if request.method == 'POST':
        if form.is_valid():

            # Get form data
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Compose email
            subject = f"{subject}"
            email_message = (f"Email: {email}\n"
                             f"Subject: {subject}\n"
                             f"Message: {message}")
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
        'subject': subject,
        'email_sent': email_sent,
        'key_skills': key_skills,
        'tech_skills': tech_skills,
    })

    return render(request, 'home.html', context)
