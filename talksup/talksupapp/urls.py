from django.urls import path

# from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login')
]