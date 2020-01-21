from django.urls import path,  include
from orient_advances.views import views

urlpatterns = [
    path('home/', views.index, name='home'),
    path('', views.index, name='home0'),
    path('home/advance', views.advance_request, name='advance'),
]
