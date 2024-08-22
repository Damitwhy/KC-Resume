from django.contrib import admin
from .models import User, ContactMessage, Skill

admin.site.register(User)
admin.site.register(ContactMessage)
admin.site.register(Skill)