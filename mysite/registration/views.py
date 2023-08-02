from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.views.generic import TemplateView

class RegistrationView(TemplateView):
    template_name = 'registration/registration.html'

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registration.html', {'form': form})

from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('send_message')
        else:
            error_message = "Invalid username or password."
            return render(request, 'registration/login.html', {'error_message': error_message})
    return render(request, 'registration/login.html')

def home(request):
    # Додайте код для відображення вашої головної сторінки тут
    return redirect('/login/')