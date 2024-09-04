from django.shortcuts import render, redirect, get_object_or_404
from .models import ContactInfo, EducationInfo, ExpertiseInfo, LanguageInfo, AboutMeInfo, Reference, User, Recommendation
from .forms import ContactMessageForm
from django.contrib import messages

def home(request):
    user = User.objects.get(username='Ken')
    contact_info = ContactInfo.objects.filter(user=user).first()
    education_info = EducationInfo.objects.filter(user=user)
    expertise_info = ExpertiseInfo.objects.filter(user=user)
    language_info = LanguageInfo.objects.filter(user=user)
    about_me_info = AboutMeInfo.objects.filter(user=user).first()
    references = Reference.objects.filter(user=user)
    recommendations = Recommendation.objects.all()

    context = {
        'contact_info': contact_info,
        'education_info': education_info,
        'expertise_info': expertise_info,
        'language_info': language_info,
        'about_me_info': about_me_info,
        'references': references,
        'recommendations': recommendations,
    }
    return render(request, 'core/home.html', context)

def projects(request):
    # Renders the projects page template
    return render(request, 'core/projects.html')

def contact(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            contact_message = form.save(commit=False)
            if request.user.is_authenticated:
                contact_message.user = request.user
            contact_message.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')  # Redirect to the same page or another page
    else:
        form = ContactMessageForm()

    return render(request, 'core/contact.html', {'form': form})
