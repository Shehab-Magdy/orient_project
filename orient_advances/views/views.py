from django.shortcuts import redirect, render
from orient_advances.forms import AdvanceForm, ExpensForm, SectionForm
from user_management.models import Account

from django.contrib import messages

def index(request):
    return render(request,'orient_advances/index.html')

def adv_about(request):
    return render(request,'about.html')

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

def other_request(request):
    return render(request,'orient_advances/other_request.html')

def add_section(request):
    context = {}
    if request.POST:
        form = SectionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Department added successfully.')
            return redirect('section_list')
        else:
            context['Section_Form']=form
    else:
        form = SectionForm()
        context['Section_Form']=form
    return render(request,'orient_advances/section_form.html',context)

def list_section(request):
    pass

def add_expens_type(request):
    context = {}
    if request.POST:
        form = ExpensForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Department added successfully.')
            return redirect('expens_list')
        else:
            context['Expens_Form']=form
    else:
        form = ExpensForm()
        context['Expens_Form']=form
    return render(request,'orient_advances/expens_form.html',context)

def list_expens(request):
    pass
