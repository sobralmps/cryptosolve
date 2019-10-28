from django.shortcuts import render, redirect

def homepage(request):
    return render(request, 'crypto/homepage.html')

def menu(request):
    return render(request, 'crypto/menu.html')