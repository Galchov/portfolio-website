from django.shortcuts import render, HttpResponse
from .models import Profile, Skill, Education, Contact
from django.core.mail import send_mail
from .forms import ContactForm


def home(request):
    key_skills = Skill.objects.filter(is_key_skill=True)
    tech_skills = Skill.objects.filter(is_key_skill=False)

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            send_mail(
                f"Message from {name}",
                message,
                email,
                ['your-email@example.com'],
                fail_silently=False,
            )
            return render(request, 'home.html', {
                'form': form,
                'success': True,
                'key_skills': key_skills,
                'tech_skills': tech_skills,
            })
    else:
        form = ContactForm()

    return render(request, 'home.html', {
        'form': form,
        'key_skills': key_skills,
        'tech_skills': tech_skills,
    })
