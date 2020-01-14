from django.urls import path,  include
from orient_advances.views import views

urlpatterns = [
    path('home/', views.index, name='home'),
    path('', views.index, name='home0'),
]
