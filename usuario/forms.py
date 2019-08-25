from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms.models import ModelForm

from .models import ModelProfile


class FormLogin(forms.Form):
    from django.contrib.auth import authenticate

    username = forms.CharField(label='Usuário')
    password = forms.CharField(widget=forms.PasswordInput, label='Senha')

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = self.authenticate(username=username, password=password)

            if not user:
                raise forms.ValidationError("Usuário não encontrado")
            elif not user.check_password(password):
                raise forms.ValidationError("Senha incorreta")
            elif not user.is_active:
                raise forms.ValidationError("Este usuário está desativado")

            return super(FormLogin, self).clean(*args, **kwargs)



class FormUser(UserCreationForm):

    email = forms.EmailField(required=True, label='E-Mail')
    first_name = forms.CharField(required=True, label='Nome')
    last_name = forms.CharField(required=True, label='Sobrenome')

    class Meta:
        model = User
        fields=['username', 'email', 'password1', 'password2', 'first_name', 'last_name']


class FormUserUpdate(forms.Form):
    email = forms.EmailField(required=True, label='E-Mail')
    first_name = forms.CharField(required=True, label='Nome')
    last_name = forms.CharField(required=True, label='Sobrenome')

    email.widget.attrs['class'] = 'form-control'
    first_name.widget.attrs['class'] = 'form-control'
    last_name.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']

    def clean_email(self, user):
        email = self.cleaned_data.get('email')
        search_user = User.objects.filter(email=email)

        if search_user:
            if search_user.username != user.username:
                raise forms.ValidationError("Este e-mail já está sendo usado.")



class FormProfile(ModelForm):

    CHOICES_CIDADES = [
        ('PF','PASSO FUNDO'),
    ]

    foto = forms.ImageField(label='Foto de perfil')
    cidade = forms.ChoiceField(required=True, label='Cidade', initial='PASSO FUNDO', choices=CHOICES_CIDADES)
    bairro = forms.CharField(max_length=50, required=True, label='Bairro')
    data_nascimento = forms.DateField(label='Aniversário')

    facebook = forms.URLField(label='Perfil do Facebook')
    twitter = forms.URLField(label='Perfil do Twitter')
    instagram = forms.URLField(label='Perfil do Instagram')
    linkedin = forms.URLField(label='Perfil do LinkedIn')
    website = forms.URLField(label='Site')

    cidade.widget.attrs['class'] = 'form-control'
    bairro.widget.attrs['class'] = 'form-control'
    data_nascimento.widget.attrs['class'] = 'form-control'
    facebook.widget.attrs['class'] = 'form-control'
    twitter.widget.attrs['class'] = 'form-control'
    instagram.widget.attrs['class'] = 'form-control'
    linkedin.widget.attrs['class'] = 'form-control'
    website.widget.attrs['class'] = 'form-control'

    class Meta:
        model = ModelProfile
        fields = ['foto', 'cidade', 'bairro', 'data_nascimento', 'facebook', 'twitter', 'instagram',
                  'linkedin', 'website']
