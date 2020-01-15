from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def profile_view(request):
    return render(request,'user_management/profile.html')
