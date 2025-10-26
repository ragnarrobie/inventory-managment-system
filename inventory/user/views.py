from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db import IntegrityError
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm  
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Account created successfully!")
                return redirect('dashboard-index')
            except IntegrityError:
                messages.error(request, "This username is already taken. Please choose another.")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CreateUserForm()

    return render(request, 'user/register.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('user-login')

@login_required
def profile(request):
    return render(request, 'user/profile.html')

@login_required
def settings(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile) 
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('user-profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'user/settings.html', context)