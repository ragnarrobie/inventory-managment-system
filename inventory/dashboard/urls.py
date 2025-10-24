from django.urls import path
from . import views
urlpatterns = [
    path('dashboard/',views.index,name='dashboard-index'),
    path('staff/',views.staff, name='dashboard-staff'),
    path('product/',views.products,name='dashboard-product'),
    path('order/',views.order,name='dashboard-order'),
     path('staff-admin/', views.staff_admin, name='dashboard-staff-admin'),
]