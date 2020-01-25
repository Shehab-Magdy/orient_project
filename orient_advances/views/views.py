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
            submit = form.save(commit=False)
            submit.emplyee_id = request.user
            submit.amount = form.cleaned_data.get('amount')
            submit.request_date = form.cleaned_data.get('request_date')
            submit.save()
            messages.success(request, f'Finance Advance Request created for {request.user}.')
            return redirect('to_pdf')
        else:
            context['Advance_Form']=form
    else:
        form = AdvanceForm()
        context['Advance_Form']=form
    return render(request,'orient_advances/advance_request.html',context)
