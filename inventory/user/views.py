from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db import IntegrityError
from .forms import CreateUserForm
from django.contrib.auth import logout


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