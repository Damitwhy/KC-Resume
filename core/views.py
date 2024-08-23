import os
from django.shortcuts import render

# Create your views here.
def home(request):
    # Renders the home page template
    return render(request, 'core/home.html')

def projects(request):
    # Renders the projects page template
    return render(request, 'core/projects.html')

def contact(request):
    # Renders the contact page template
    return render(request, 'core/contact.html')

