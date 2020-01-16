from django.shortcuts import render, redirect
from django.contrib import messages
from user_management.forms.register_form import UserRegisterForm
from orient_advances.models import Section
from django.contrib.auth.models import User

def register_view(request):
    sections = Section.objects.all()
    if request.POST:
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            newUser = User()
            newUser.email = request.POST.get('email')
            newUser.username = request.POST.get('username')
            newUser.password = request.POST.get('password1')
            newUser.Profile.fullname = request.POST.get('fullname')
            newUser.Profile.employee_id = request.POST.get('employee_id')
            newUser.Profile.section = request.POST.get('section')
            newUser.Profile.is_boss = True if request.POST.get('section-dd') else False

            messages.success(request, f'Account created for {newUser.username}, You can now login.')
            print('success')
            # newUser.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'user_management/registration.html',{'form':form,'sections':sections})
