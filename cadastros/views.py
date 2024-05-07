from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def ap_input(request):
    return render(request, 'pag002.html')

def consult(request):
    return render(request, 'pag003.html')

def pending_docs(request):
    return render(request, 'pag004.html')

def closing(request):
    return render(request, 'pag005.html')

# Create your views here.
