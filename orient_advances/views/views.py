from django.shortcuts import render

def index(request):
    return render(request,'orient_advances/index.html')