from django.urls import path

# from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('podcasts', views.podcasts, name='podcasts'),
    path('newPodcast', views.newPodcast, name='newPodcast'),
    path('updatePodcast/<int:id>', views.updatePodcast, name='updatePodcast'),
    path('deletePodcast/<int:id>', views.deletePodcast, name = 'deletePodcast')
]