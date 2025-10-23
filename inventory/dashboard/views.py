from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required

# Create your views here.

def superuser_required(view_func):
    """Decorator that checks if the user is a superuser."""
    def wrapper(request, *args, **kwargs):
        if not request.user.is_superuser:
            # Redirect staff users to staff page, others see access denied
            if request.user.is_staff:
                from django.shortcuts import redirect
                return redirect('dashboard-staff')
            return render(request, 'dashboard/index.html')
        return view_func(request, *args, **kwargs)
    return wrapper

@login_required(login_url='user-login')
@superuser_required
def index(request):
    return render(request, 'dashboard/index.html')

@login_required(login_url='user-login')
def staff(request):
    # Only staff and superusers can access this page
    if not (request.user.is_staff or request.user.is_superuser):
        return render(request, 'dashboard/index.html')
    return render(request, 'dashboard/staff.html')

@login_required(login_url='user-login')
def products(request):
    return render(request,'dashboard/product.html')

@login_required(login_url='user-login')
def order(request):
    return render(request,'dashboard/order.html')