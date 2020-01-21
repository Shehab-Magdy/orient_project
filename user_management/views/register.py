from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from user_management.forms import RegistrationForm
from django.contrib import messages


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            row_password = form.cleaned_data.get('password1')
            username = form.cleaned_data.get('username')
            account = authenticate(email = email, password=row_password)
            login(request,account)
            messages.success(request, f'Account created for {username}, You can now login.')
            return redirect('login')
        else:
            context['registration_form']=form
    else:
        form = RegistrationForm()
        context['registration_form']=form
    return render(request,'user_management/registration.html',context)