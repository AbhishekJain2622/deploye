import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

User = get_user_model()
username = os.environ.get('Abhishek')
email = os.environ.get('aj482522@gmail.com')
password = os.environ.get('Abhi@2002')

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)