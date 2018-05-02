from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html') #{'firstname': request.user.first_name})

def signup_view(request):
    if request.method == 'GET':
        return render(request, 'registration/register.html', {})
