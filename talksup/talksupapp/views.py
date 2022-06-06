from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as djLogin, logout as djLogout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import Podcast
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the talksupapp index.")

def login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        user = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=user, password=password)
        if user is not None:
            djLogin(request, user)
            return redirect('dashboard')
        else:
            return render(request, "talksupapp/login.html", {"mensaje": "Usuario o contraseña incorrectos"})
    return render(request, "talksupapp/login.html")

def logout(request):
    djLogout(request)
    return render(request, "talksupapp/login.html")
    
@login_required(login_url='login')
def dashboard(request):
    return render(request, 'talksupapp/dashboard.html')

@login_required(login_url='login')
def podcasts(request):
    allObjects = Podcast.objects.all()
    return render(request, 'talksupapp/podcasts.html', {"podcasts": allObjects})