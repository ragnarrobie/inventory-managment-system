from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class CreateUserForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']  # Added first_name and last_name

class ProfileUpdateForm(forms.ModelForm):  # Fixed typo: ProfileUpfateForm to ProfileUpdateForm
    class Meta:
        model = Profile
        fields = ['address', 'phone', 'image']