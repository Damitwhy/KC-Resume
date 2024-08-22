import os
from django.shortcuts import render

# Create your views here.
def home(request):
    # Renders the home page template
    return render(request, 'core/home.html')