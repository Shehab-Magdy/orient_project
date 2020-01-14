from django.shortcuts import render, redirect
from django.contrib import messages


def profile_view(request):
    return render(request,'user_management/profile.html')
