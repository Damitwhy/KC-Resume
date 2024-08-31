from django.shortcuts import render
from .models import ContactInfo, EducationInfo, ExpertiseInfo, LanguageInfo, AboutMeInfo, Reference, User

def home(request):
    user = User.objects.get(username='Ken')
    contact_info = ContactInfo.objects.filter(user=user).first()
    education_info = EducationInfo.objects.filter(user=user)
    expertise_info = ExpertiseInfo.objects.filter(user=user)
    language_info = LanguageInfo.objects.filter(user=user)
    about_me_info = AboutMeInfo.objects.filter(user=user).first()
    references = Reference.objects.filter(user=user)

    context = {
        'contact_info': contact_info,
        'education_info': education_info,
        'expertise_info': expertise_info,
        'language_info': language_info,
        'about_me_info': about_me_info,
        'references': references,
    }
    return render(request, 'core/home.html', context)

def projects(request):
    # Renders the projects page template
    return render(request, 'core/projects.html')

def contact(request):
    # Renders the contact page template
    return render(request, 'core/contact.html')


