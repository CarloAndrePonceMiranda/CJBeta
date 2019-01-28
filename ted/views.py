#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login, logout, get_user_model
from plantillas.models import Plantilla
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from plantillas.models import Plantilla
from .forms import ContactForm, LoginForm, RegisterForm
import datetime
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.views.generic.detail import DetailView
from datetime import date
from django.conf import settings
from django.core.mail import send_mail


import time
User = get_user_model()

class AuthDetail(DetailView):
    model = User
    fields = ['id','username', 'password', 'first_name','last_name','last_login','is_active','is_staff','is_superuser']
class AuthUpdate(UpdateView):
    model = User
    success_url = reverse_lazy('users')
    fields = ['id','username', 'first_name','last_name','email','is_active','is_superuser','is_staff']
class AuthDelete(DeleteView):
    model = User
    success_url = reverse_lazy('users')

def home_page(request):
    usuario = User
    queryset = Plantilla.objects.all().order_by('nombre')
    context = {
        'titulo':"This Engineers Develop",
        'queryset':queryset
    }
    return render(request, "home_page.html", context)

def reportes(request):
    return render(request, "reportes/reportes.html")

def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_email =  form.cleaned_data.get("email")
        form_mensaje =  form.cleaned_data.get("mensaje")
        form_nombre =  form.cleaned_data.get("nombre")
        asunto = 'No Responder This Engineers Develop'
        email_from = settings.EMAIL_HOST_USER
        email_to = [form_email]
        email_mensaje = "No Responder, hola %s, mensaje: %s Nos pondremos en contacto al correo %s" %(form_nombre,form_mensaje,form_email)
        send_mail(asunto,
            email_mensaje,
            email_from,
            email_to,
            fail_silently=False,
            )
            # print email,mensaje,nombre
    context = {'form': form}
    return render(request,"generales/contacto.html",context)

def about_page(request):
    context = {
        "title":"Acerca de",
        "content": "Welcome to about page"
    }
    return render(request, "generales/about_page.html", context)

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        'form':form
    }
    print(request.user.is_authenticated())
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("usuario")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            # context['form'] = LoginForm()
            return redirect("/")
            print(request.user.is_authenticated())
        else:
            print("error")
    return render(request, "auth/login.html",context)



def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form':form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        usuario_nuevo = User.objects.create_user(username,email,password)
        messages.info(request, 'Usuario Registrado Exitosamente!')
        print(usuario_nuevo)
    return render(request, "auth/register.html",context)

def lista_de_usuarios(request):
    queryset = User.objects.all().order_by('id')
    context = {
        'queryset':queryset
    }
    return render(request, "auth/list.html",context)

def lista_pweb(request):
    queryset = Plantilla.objects.all().order_by('nombre').filter(categoria='Páginas Web')
    context = {
        'queryset':queryset
    }
    return render(request, "generales/list-pweb.html",context)

def lista_sweb(request):
    queryset = Plantilla.objects.all().order_by('nombre').filter(categoria='Sistemas Web')
    context = {
        'queryset':queryset
    }
    return render(request, "generales/list-sweb.html",context)
