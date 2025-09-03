import django.forms as forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import re
import dns.resolver


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        def name(self):
            username= self.cleaned_data.get('username')
            if not re.match(r'[a--zA-Z]+$', username):
                raise forms.ValidationError('O nome de usuário só pode conter letras') 
            if len(username) < 20:
                raise forms.ValidationError('O nome de usuário deve ter pelo menos 20 caracteres')
            return username
        
        def senha(self):
            password= self.cleaned_data.get('password1')
            if len(password) < 8:
                raise forms.ValidationError('A senha deve ter pelo menos 8 caracteres')
            if password.isdigit():
                raise forms.ValidationError('A senha não pode ser totalmente numérica')
            return password
        
        def email(self):
            email= self.cleaned_data.get('email')
            domain = email.split('@')[1]
            try:
                dns.resolver.resolve(domain, 'MX')
            except dns.resolver.NXDOMAIN:
                raise forms.ValidationError('O domínio do email não existe')
            except dns.resolver.NoAnswer:
                raise forms.ValidationError('O domínio do email não possui registros MX')
            return email

        labels = {
            'username': 'Nome de Usuário',
            'email': 'Email',
            'password1': 'Senha',
            'password2': 'Confirmação de Senha',
        }
