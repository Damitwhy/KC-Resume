# Generated by Django 5.0.7 on 2024-09-04 14:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_contactmessage_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('connection_type', models.CharField(max_length=100)),
                ('education', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('relationship', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('contact_link', models.URLField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recommendations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
