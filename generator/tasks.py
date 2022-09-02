import os

from celery import shared_task
from hashlib import sha256

from django.conf import settings

from .utils import send_email, edit_image

@shared_task
def send_certificate(name: str, email: str):
    image_name = sha256(f'{name}{email}'.encode()).hexdigest()
    path = os.path.join(settings.BASE_DIR, f'media/certificates/{image_name}.png')

    edit_image(name, image_name)
    send_email(settings.TEMPLATE_PATH, 'Atestado', email, name=name, path=path)

    return True
