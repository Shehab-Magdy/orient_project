from django.urls import path,  include
from django.contrib.auth import views as auth_view
from user_management.views import register,profile

urlpatterns = [
    path('register/', register.register_view,name='register'),
    path('profile/', profile.profile_view,name='profile'),
    path('login/', auth_view.LoginView.as_view(template_name='user_management/login.html'),name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='user_management/logout.html'),name='logout'),
]
