from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.


def view_success_data(request,view,frase):

    messages.success(request, frase)
    return redirect(view)


def view_success(request):
  pass