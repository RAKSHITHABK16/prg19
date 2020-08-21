import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","prg19.settings")

import django
django.setup()

from django.core.files.storage import FileSystemStorage

def store_image(image):
    fs=FileSystemStorage()
