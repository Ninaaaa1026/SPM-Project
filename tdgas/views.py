from django.shortcuts import render

from .models import DOG_TYPE

def home_view(request):
    return render(request, 'home.html', {'firstname': request.user.first_name})

def signup_view(request):
    if request.method == 'GET':
        return render(request, 'registration/register.html', {})
    if request.method == 'POST':
        pass

def user_profile_view(request):
    if request.method == 'GET':
        dog_breeds = DOG_TYPE
        return render(request, 'user_profile.html', {'firstname': request.user.first_name,
                                                     'breeds'   : dog_breeds})
    if request.method == 'POST':
        pass

def dog_add_view(request):
    if request.method == 'POST':
        pass