from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='dashboard-index'),
    path('staff/',views.staff, name='dashboard-staff'),
    path('product/',views.products,name='dashboard-product'),
    path('order/',views.order,name='dashboard-order'),
]