from django.shortcuts import render, redirect
from django.contrib import messages
from user_management.forms.register_form import UserRegisterForm
from orient_advances.models import Section

def register_view(request):
    sections = Section.objects.all()
    if request.POST:
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}, You can now login.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'user_management/registration.html',{'form':form,'sections':sections})
