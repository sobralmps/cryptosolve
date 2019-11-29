from django.shortcuts import render, redirect


def homepage(request):
    return render(request, 'crypto/home.html')


def menu(request):
    return render(request, 'crypto/menu.html')


def congrats(request):
    return render(request, 'crypto/congrats.html')


def endgame(request):
    return render(request, 'crypto/endgame.html')


def faq(request):
    return render(request, 'crypto/faq.html')


def cont(request):
    return render(request, 'crypto/contato.html')
