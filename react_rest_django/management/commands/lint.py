"""Command handler for lint on the whole project."""
import os
import subprocess
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    """Command handler for lint on the whole project."""
    help = 'Runs lint on all the source code of the project.'

    def handle(self, *args, **options):
        modules = [o for o in os.listdir('.')
                   if os.path.isdir(o) and os.path.exists(o+'/__init__.py')]
        ret = subprocess.call(['pylint', '-rn'] + modules)
        if ret:
            raise CommandError("Code not pylint clean (%d)" % ret)
