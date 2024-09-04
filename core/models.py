from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

class ContactMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contact_messages', null=True, blank=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"

class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skills')
    skill_name = models.CharField(max_length=255)
    proficiency_level = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.skill_name} ({self.proficiency_level})"

class ContactInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='contact_info')
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    location = models.CharField(max_length=100)

class EducationInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='education_info')
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)

class ExpertiseInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expertise_info')
    skill = models.CharField(max_length=50)

class LanguageInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='language_info')
    language = models.CharField(max_length=50)

class AboutMeInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='about_me_info')
    description = models.TextField()

class Reference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='references')
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    relationship = models.CharField(max_length=100)

class Recommendation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recommendations')
    name = models.CharField(max_length=100)
    connection_type = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    date = models.DateField()
    relationship = models.CharField(max_length=100)
    text = models.TextField()
    contact_link = models.URLField()

    def __str__(self):
        return f"Recommendation by {self.name}"