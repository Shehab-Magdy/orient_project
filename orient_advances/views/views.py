from django.shortcuts import redirect, render
from orient_advances.forms import AdvanceForm, ExpensForm, SectionForm, otherForm
from orient_advances.models import Section, Expens
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
    context = {}
    if request.POST:
        form = otherForm(request.POST)
        if form.is_valid():
            submit = form.save(commit=False)
            submit.emplyee_id = request.user
            submit.amount = form.cleaned_data.get('amount')
            submit.request_date = form.cleaned_data.get('request_date')
            submit.description = form.cleaned_data.get('description')
            submit.save()
            messages.success(request, f'Request created for {request.user}.')
            return redirect('to_pdf')
        else:
            context['other_Form']=form
    else:
        form = otherForm()
        context['other_Form']=form
    return render(request,'orient_advances/other_request.html',context)

def add_section(request):
    context = {}
    if request.POST:
        form = SectionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Department successfully added.')
            return redirect('department_list')
        else:
            context['Section_Form']=form
    else:
        form = SectionForm()
        context['Section_Form']=form
    return render(request,'orient_advances/section_form.html',context)

def list_section(request):
    context = {}
    sections = Section.objects.all()
    context['sections']=sections
    return render(request,'orient_advances/section_list.html',context)
    

def add_expens_type(request):
    context = {}
    if request.POST:
        form = ExpensForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Expense type added successfully.')
            return redirect('expenses_list')
        else:
            context['Expens_Form']=form
    else:
        form = ExpensForm()
        context['Expens_Form']=form
    return render(request,'orient_advances/expens_form.html',context)

def list_expens(request):
    context = {}
    expens = Expens.objects.all()
    context['expenses']=expens
    return render(request,'orient_advances/expens_list.html',context)
