from django.forms import ModelForm, widgets
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

from django.utils.translation import gettext_lazy as _


class MyUserCreationForm(UserCreationForm):
  password1 = forms.CharField(
      label=_("Your Password"),
      widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
  )
  password2 = forms.CharField(
      label=_("Confirm Password"),
      widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
  )

  class Meta:
    model = User
    fields = ('username', 'email', )

    labels = {
      'username': _('Your Username'),
      'email': _('Your Email'),
    }
    widgets = {
      'username': forms.TextInput(attrs={
          'class': 'form-control',
          'placeholder': 'Username'
      }),
      'email': forms.EmailInput(attrs={
          'class': 'form-control',
          'placeholder': 'example@company.com'
      })
    }