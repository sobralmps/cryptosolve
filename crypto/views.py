from django.shortcuts import render, redirect

def home(request):
    return render(request, 'crypto/home.html')

def menu(request):
    return render(request, 'crypto/menu.html')