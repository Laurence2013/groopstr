from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)

class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label = 'Email Address')
    email2 = forms.EmailField(label = 'Confirm Email')
    password = forms.CharField(widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'email2', 'password']

    def clean_email2(self):
        email = self.cleaned_data.get('email')
        confirm_email = self.cleaned_data.get('email2')

        if email != confirm_email:
            raise forms.ValidationError('Email address must match')
        return email
