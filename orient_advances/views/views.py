from django.shortcuts import redirect, render
from orient_advances.forms import AdvanceForm
from user_management.models import Account

from django.contrib import messages

def index(request):
    return render(request,'orient_advances/index.html')

def advance_request(request):
    context = {}
    if request.POST:
        form = AdvanceForm(request.POST)
        if form.is_valid():
            username = request.username
            form.emplyee = Account.objects.get(username=request.username)
            form.save()
            messages.success(request, f'Finance Advance Request created for {username}.')
            return redirect('home')
        else:
            context['Advance_Form']=form
    else:
        form = AdvanceForm()
        context['Advance_Form']=form
    return render(request,'orient_advances/advance_request.html',context)