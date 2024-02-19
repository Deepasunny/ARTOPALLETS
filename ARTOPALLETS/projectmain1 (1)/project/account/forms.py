from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput(attrs={'class': 'contactus', 'placeholder': 'Password'}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(
        attrs={'class': 'contactus', 'placeholder': 'Confirm Password'}))
    email = forms.CharField(required=True,
                            widget=forms.EmailInput(attrs={'class': 'contactus', 'placeholder': 'Email Address'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'email': 'Email'}
        widgets = {'username': forms.TextInput(attrs={'class': 'contactus', 'placeholder': 'Username'})}


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={
        'autofocus': True,
        'class': 'contactus',
        'placeholder': 'Username'
    }))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={
        'autocomplete': 'current-password',
        'class': 'contactus',
        'placeholder': 'Password'
    }))


from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'image_file']
