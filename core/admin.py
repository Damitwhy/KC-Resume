from django.contrib import admin
from .models import User, ContactMessage, Skill, ContactInfo, EducationInfo, ExpertiseInfo, LanguageInfo, AboutMeInfo, Reference

admin.site.register(User)
admin.site.register(ContactMessage)
admin.site.register(Skill)
admin.site.register(ContactInfo)
admin.site.register(EducationInfo)
admin.site.register(ExpertiseInfo)
admin.site.register(LanguageInfo)
admin.site.register(AboutMeInfo)
admin.site.register(Reference)