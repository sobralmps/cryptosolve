from django.shortcuts import render, redirect


def homepage(request):
    return render(request, 'crypto/home.html')


def menu(request):
    return render(request, 'crypto/menu.html')


def congrats(request):
    return render(request, 'crypto/congrats.html')


def fim(request):
    return render(request, 'crypto/fim.html')


def faq(request):
    return render(request, 'crypto/faq.html')


def cont(request):
    return render(request, 'crypto/contato.html')


def fase01(request):
    return render(request, 'crypto/fase01.html')


def instrucoes(request):
    return render(request, 'crypto/instrucoes.html')


def embreve(request):
    return render(request, 'crypto/embreve.html')


def ajuda1(request):
    return render(request, 'crypto/ajuda1.html')


def ajuda2(request):
    return render(request, 'crypto/ajuda2.html')


def ajuda3(request):
    return render(request, 'crypto/ajuda3.html')


def comojogar(request):
    return render(request, 'crypto/comojogar.html')
