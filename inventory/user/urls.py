from django.urls import path,include
from user import views as user_view
from django.contrib.auth import views as auth_views

urlpatterns = [  
    path('register/', user_view.register, name='user-register'),
    path('', auth_views.LoginView.as_view(template_name='user/login.html'), name='user-login'),
    path('logout/', user_view.user_logout, name='user-logout'),
     path('profile/', user_view.profile, name='user-profile'),
     path('settings',user_view.settings,name='user-settings'),
]