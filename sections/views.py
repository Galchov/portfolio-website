from django.shortcuts import render, redirect
from .models import Profile, Skill, Education, Contact
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm


def home(request):
    key_skills = Skill.objects.filter(is_key_skill=True)
    tech_skills = Skill.objects.filter(is_key_skill=False)
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            send_mail(
                f"Message from {name}",
                message=message,
                from_email=email,
                recipient_list=[],
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('home')

    return render(request, 'home.html', {
        'form': form,
        'key_skills': key_skills,
        'tech_skills': tech_skills,
    })
