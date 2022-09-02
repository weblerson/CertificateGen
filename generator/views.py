from django.shortcuts import render, redirect

from .forms import CertificateForm
from .tasks import send_certificate

def generate_certificate(request):
    match request.method:
        case 'GET':
            form = CertificateForm()
            context = {'form': form}

            return render(request, 'generate_certificate.html', context)

        case 'POST':
            form = CertificateForm(request.POST)
            if form.is_valid():
                name = form.data.get('nome')
                email = form.data.get('email')

                try:
                    send_certificate.delay(name, email)

                    return redirect('/?status=1')

                except:
                    return redirect('/?status=2')