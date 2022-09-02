from django import forms

class CertificateForm(forms.Form):
    nome = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=60)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.get('nome').widget.attrs.update({'class': 'form-control'})
        self.fields.get('email').widget.attrs.update({'class': 'form-control'})

        self.fields.get('nome').widget.attrs.update({'placeholder': 'Ex.: Weblerson'})
        self.fields.get('email').widget.attrs.update({'placeholder': 'Ex.: lerson@gmail.com'})

        self.fields.get('nome').label = 'Nome:'
        self.fields.get('email').label = 'E-mail:'