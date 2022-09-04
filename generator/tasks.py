from celery import shared_task
from hashlib import sha256

from django.conf import settings

from .utils import send_email, edit_image

@shared_task(name='send_certificate', bind=True, max_retries=5, default_retry_delay=2)
def send_certificate(self, name: str, email: str):
    image_name = sha256(f'{name}{email}'.encode()).hexdigest()

    try:
        edit_image(name, image_name)
        send_email(settings.TEMPLATE_PATH, 'Atestado', email, name=name, image_name=image_name)

        return True

    except:
        self.retry(countdown=2*self.request.retries)
        
        raise Exception('An error has occurred.')
