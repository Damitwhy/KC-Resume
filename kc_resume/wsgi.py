"""
WSGI config for kc_resume project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

# import os
# import sys

# from django.core.wsgi import get_wsgi_application

# # Add the project directory to the sys.path
# sys.path.append('/var/www/html/purerarez.co.uk/KC-Resume')
# sys.path.append('/var/www/html/purerarez.co.uk/KC-Resume/kc_resume')

# # Activate the virtual environment
# activate_this = '/var/www/html/purerarez.co.uk/KC-Resume/venv/bin/activate_this.py'
# with open(activate_this) as file_:
#     exec(file_.read(), dict(__file__=activate_this))

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kc_resume.settings')

# application = get_wsgi_application()

import os
import sys

from django.core.wsgi import get_wsgi_application

# Update this path to the correct virtual environment activation script
activate_this = '/workspace/KC-Resume/venv/bin/activate_this.py'

# If the activate_this.py file exists, execute it
if os.path.exists(activate_this):
    exec(open(activate_this).read(), {'__file__': activate_this})

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kc_resume.settings')

application = get_wsgi_application()