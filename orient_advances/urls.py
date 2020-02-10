from django.urls import path,  include
from django.conf.urls import url
from orient_advances.views import views, GeneratePdf

urlpatterns = [
    path('home/', views.index, name='home'),
    path('about/', views.adv_about, name='advance_about'),
    path('', views.index, name='home0'),
    path('pdf/',GeneratePdf.GeneratePdf.as_view(),name='to_pdf'),
    path('home/advance', views.advance_request, name='advance'),
    path('home/other', views.other_request, name='other'),
    path('home/department', views.list_section, name='department_list'),
    path('home/adddepartment', views.add_section, name='department_new'),
    path('home/expense', views.list_expens, name='expenses_list'),
    path('home/addexpense', views.add_expens_type, name='expenses_new'),
]
