# users/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)



    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email):
            print('Cet email est déjà utilisé. Veuillez recommencer.')
            raise forms.ValidationError('Cet email est déjà utilisé. Veuillez recommencer.')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            print('Les mots de passe ne correspondent pas. Veuillez les saisir à nouveau.')
            raise forms.ValidationError('Les mots de passe ne correspondent pas. Veuillez les saisir à nouveau.')
        return password2
