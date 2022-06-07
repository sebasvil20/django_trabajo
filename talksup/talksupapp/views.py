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

@login_required(login_url='login')
def newPodcast(request):
    if request.method == 'POST':
        name = request.POST['podName']
        description = request.POST['podDescription']
        urlCover = request.POST['podURL']
        epQuantity = request.POST['podEpisodes']
        rDate = request.POST['podReleaseDate']
        try:
            podcast = Podcast.objects.create(
                name= name,
                description = description,
                cover_pic_url = urlCover,
                total_episodes = epQuantity,
                release_date = rDate
            )
            podcast.save()
        except:
            return render(request, 'talksupapp/podcastForm.html', {"mensaje": "No se pudo crear, intentelo de nuevo"})
        return redirect('podcasts')
    return render(request, 'talksupapp/podcastForm.html')


@login_required(login_url='login')
def updatePodcast(request, id):
    podcast = Podcast.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST['podName']
        description = request.POST['podDescription']
        urlCover = request.POST['podURL']
        epQuantity = request.POST['podEpisodes']
        try:
            podcast.name = name
            podcast.description = description
            podcast.cover_pic_url = urlCover
            podcast.total_episodes = epQuantity
            podcast.release_date = podcast.release_date
            podcast.save()
        except:
            return render(request, 'talksupapp/editForm.html', {"podcast": podcast, "mensaje": "No se pudo actualizar, intentelo de nuevo"})
        return redirect('podcasts')
    return render(request, 'talksupapp/editForm.html', {"podcast": podcast})



@login_required(login_url='login')
def deletePodcast(request, id):
    try:
        Podcast.objects.get(id=id).delete()
    except:
        return redirect('podcasts')

    return redirect('podcasts')