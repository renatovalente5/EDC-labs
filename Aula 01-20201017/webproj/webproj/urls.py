"""webproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('hello/', views.hello, name='hello'),
    path('home/', views.home, name='home'),

################################# AULA 1 #######################################
    path('numero/<int:num>/', views.numero, name='numero'),
    path('numerot/<int:num>/', views.numerot, name='numerot'),
    path('info/', views.info, name='info'),
    path('sendinfo/', views.sendinfo, name='sendinfo'),

################################# AULA 2 #######################################
    path('xml_view/', views.xml_view, name='xml_view'),

################################# AULA 3 #######################################
    path('cursos/', views.cursos, name='cursos'),
    path('curso/', views.curso, name='curso'),
    path('cursoDepart/', views.cursospordepart, name='cursoDepart'),
    path('departamento/', views.departamento, name='departamento'),

################################# AULA 4 #######################################
    path('addExample/', views.addExample, name='addExample'),

################################# AULA 5 #######################################
    path('pageRSS/', views.pageRSS, name='pageRSS'),
]
