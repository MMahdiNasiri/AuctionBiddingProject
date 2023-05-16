from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    username = forms.CharField(label='User Name',
                               widget=forms.TextInput(attrs={'autocomplete': 'off',
                                                             'class': 'form-control'}))
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput(attrs={'autocomplete': 'off',
                                                                  'class': 'form-control'}))
    password2 = forms.CharField(label='Repeat Password',
                                widget=forms.PasswordInput(attrs={'autocomplete': 'off',
                                                                  'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class LoginForm(forms.ModelForm):
    username = forms.CharField(
                               widget=forms.TextInput(attrs={'class': 'form-control col-6'}))
    password = forms.CharField(
                               widget=forms.PasswordInput(attrs={'autocomplete': 'off',
                                                                 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'password']


