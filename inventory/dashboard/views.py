from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


def superuser_required(view_func):
    """Restrict access to superusers; redirect staff or show denied."""
    def wrapper(request, *args, **kwargs):
        user = request.user
        if not user.is_superuser:
            if user.is_staff:
                # Redirect staff users to staff_admin page
                return redirect('dashboard-staff-admin')
            if user.is_active:
                return render(request, 'dashboard/access_denied.html')
            return HttpResponseForbidden("Access denied.")
        return view_func(request, *args, **kwargs)
    return wrapper


@login_required(login_url='user-login')
@superuser_required
def index(request):
    """Superuser dashboard."""
    return render(request, 'dashboard/index.html')


@login_required(login_url='user-login')
def staff_admin(request):
    """Staff admin dashboard (for staff users only)."""
    user = request.user
    if not (user.is_staff or user.is_superuser):
        return render(request, 'dashboard/access_denied.html')
    return render(request, 'dashboard/staff_admin.html')


@login_required(login_url='user-login')
def staff(request):
    """Legacy staff page (if you still need it)."""
    user = request.user
    if not (user.is_staff or user.is_superuser):
        return render(request, 'dashboard/access_denied.html')
    return render(request, 'dashboard/staff.html')


@login_required(login_url='user-login')
def products(request):
    user = request.user
    if not user.is_superuser:
        return render(request, 'dashboard/access_denied.html')
    return render(request, 'dashboard/product.html')


@login_required(login_url='user-login')
def order(request):
    user = request.user
    if not user.is_superuser:
        return render(request, 'dashboard/access_denied.html')
    return render(request, 'dashboard/order.html')
