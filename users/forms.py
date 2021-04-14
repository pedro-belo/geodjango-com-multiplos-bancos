from django.contrib.auth import forms as auth_forms
from django import forms
from django.contrib.auth import get_user_model
from core.models import Cities

UserModel = get_user_model()


class LoginForm(auth_forms.AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Usuário'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Senha'
        })


class RegisterForm(auth_forms.UserCreationForm):

    city = forms.ModelChoiceField(
        queryset=Cities.objects.all(), required=True, empty_label='Seu município')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Usuário'
        })
        self.fields['city'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Seu município'
        })
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Nome'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Senha'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Repetir senha'
        })

    class Meta:
        model = UserModel
        fields = ("username", "name",)
