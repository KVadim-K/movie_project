from django.shortcuts import render

def index(request):
    return render(request, 'films/index.html')

def new(request):
    return render(request, 'films/new.html')