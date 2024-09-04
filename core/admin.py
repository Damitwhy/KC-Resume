from django.contrib import admin
from .models import User, ContactMessage, Skill, ContactInfo, EducationInfo, ExpertiseInfo, LanguageInfo, AboutMeInfo, Reference, Recommendation

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
    search_fields = ('username', 'email')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'timestamp', 'read')
    search_fields = ('name', 'email')
    list_filter = ('read', 'timestamp')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('user', 'skill_name', 'proficiency_level')
    search_fields = ('skill_name', 'user__username')

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'email', 'location')
    search_fields = ('phone', 'email', 'location')

@admin.register(EducationInfo)
class EducationInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'degree', 'institution')
    search_fields = ('degree', 'institution')

@admin.register(ExpertiseInfo)
class ExpertiseInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'skill')
    search_fields = ('skill',)

@admin.register(LanguageInfo)
class LanguageInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'language')
    search_fields = ('language',)

@admin.register(AboutMeInfo)
class AboutMeInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'description')
    search_fields = ('description',)

@admin.register(Reference)
class ReferenceAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'contact', 'relationship')
    search_fields = ('name', 'contact', 'relationship')

@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'connection_type', 'education', 'date', 'relationship')
    search_fields = ('name', 'connection_type', 'education', 'relationship')
    list_filter = ('date',)