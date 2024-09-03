# myapp/management/commands/custom_flush.py

from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Flush the database while keeping essential tables'

    def handle(self, *args, **kwargs):
        essential_tables = ['auth_user', 'django_migrations']
        call_command('flush', '--no-input', exclude=essential_tables)