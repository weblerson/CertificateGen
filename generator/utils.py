import os

from email.mime.image import MIMEImage
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from PIL import Image
from PIL import ImageDraw

from django.conf import settings

def edit_image(name: str, image_name: str):
    img = Image.open(os.path.join(settings.BASE_DIR, 'templates/static/generator/img/ModeloAtestado.png'))
    draw = ImageDraw.Draw(img)
    draw.text((375, 175), name.title(), (0, 0, 0))
    img.save(os.path.join(settings.BASE_DIR, f'media/certificates/{image_name}.png'))

    return True

def send_email(template_path: str, subject: str, to: str, **kwargs):
    html_content = render_to_string(template_path, kwargs)
    text_content = strip_tags(html_content)
    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [to])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()

    return True