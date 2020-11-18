"""projecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('', views.index, name='index'),
    path('news/', views.news, name='news'),
    path('artist/', views.artist, name='artist'),
    path('favorites/', views.favorites, name='favorites'),
    path('trackglobal/', views.trackglobal, name='trackglobal'),
    path('trackport/', views.trackport, name='trackport'),
    path('artistglobal/', views.artistglobal, name='artistglobal'),
    path('artistport/', views.artistport, name='artistport'),
    path('fav_add/', views.fav_add, name='fav_add'),
    path('fav_remove/', views.fav_remove, name='fav_remove')
]
