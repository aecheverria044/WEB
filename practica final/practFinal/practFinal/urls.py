"""practFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from apps.usuario.views import home_view
from apps.usuario.views import contacto
from apps.usuario.views import user_detail_view
from apps.usuario.views import user_create_view
from apps.usuario.views import login
urlpatterns = [
   path('',home_view, name="home_view"),
    path('home/',home_view, name="home_view"),
    path('contacto/',contacto, name="contacto"),
    path('admin/', admin.site.urls),
    path('detailUser/',user_detail_view, name="user_detail_view"),
    path('createUser/',user_create_view, name="user_create_view"),
    path('login/',login, name="login"),
]
