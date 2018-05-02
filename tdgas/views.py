from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def registerNew(request):
    return render(request, 'registerNew.html', {})