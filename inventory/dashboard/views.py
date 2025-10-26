from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import product,Order
from .forms import ProductForm,OrderForm
from django.contrib.auth.models import User

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
    orders = Order.objects.all()
    if request.method=='POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user 
            instance.save()
            return redirect('dashboard-index')
        else:
            print("Form errors:", form.errors)
    else:
        form = OrderForm()
    context= {
        'orders': orders,
        'form' : form,
    }
    return render(request, 'dashboard/index.html',context)


@login_required(login_url='user-login')
def staff_admin(request):
    """Staff admin dashboard (for staff users only)."""
    user = request.user
    if not (user.is_staff or user.is_superuser):
        return render(request, 'dashboard/access_denied.html')

    orders = Order.objects.all()
    if request.method=='POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('dashboard-staff-admin')
    else:
        form = OrderForm()
    
    context = {
        'orders': orders,
        'form': form
    }
    return render(request, 'dashboard/staff_admin.html', context)

@login_required(login_url='user-login')
def staff(request):
    workers = User.objects.all()
    context = {
        'workers':workers
    }
    user = request.user
    if not (user.is_staff or user.is_superuser):
        return render(request, 'dashboard/access_denied.html')
    return render(request, 'dashboard/staff.html',context)

@login_required(login_url='user-login')
def staff_detail(request,pk):
    workers = User.objects.get(id=pk)
    context = {
        'worker' : workers,
    }
    return render(request,'dashboard/staff-detail.html',context)

@login_required(login_url='user-login')
def products(request):
    items = product.objects.all()
    if request.method =='POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm()
    context = {
        'items' : items,
        'form' : form,
    }
    user = request.user
    if not user.is_superuser:
        return render(request, 'dashboard/access_denied.html')
    return render(request, 'dashboard/product.html',context)
@login_required(login_url='user-login')

def product_delete(request,pk):
    item = product.objects.get(id=pk)
    if request.method== 'POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request, 'dashboard/Delete.html')

@login_required(login_url='user-login')
def product_edit(request,pk):
    item = product.objects.get(id=pk)
    if request.method=='POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')

    else:
        form = ProductForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/Edit.html', context)


@login_required(login_url='user-login')
def order(request):
    orders = Order.objects.all()
    context = {
        'orders': orders,
    }
    user = request.user
    if not user.is_superuser:
        return render(request, 'dashboard/access_denied.html')
    return render(request, 'dashboard/order.html',context)
