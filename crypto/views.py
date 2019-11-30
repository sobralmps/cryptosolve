from django.shortcuts import render, redirect


def homepage(request):
    return render(request, 'crypto/home.html')


def menu(request):
    return render(request, 'crypto/menu.html')


def congrats(request):
    return render(request, 'crypto/congrats.html')


def fim(request):
    return render(request, 'crypto/game/fim.html')


def faq(request):
    return render(request, 'crypto/faq.html')


def cont(request):
    return render(request, 'crypto/contato.html')


def fase01(request):
    return render(request, 'crypto/game/fase01.html')


def fase02(request):
    return render(request, 'crypto/game/fase02.html')


def fase03(request):
    return render(request, 'crypto/game/fase03.html')


def fase04(request):
    return render(request, 'crypto/game/fase04.html')


def fase05(request):
    return render(request, 'crypto/game/fase05.html')


def fase06(request):
    return render(request, 'crypto/game/fase06.html')


def fase07(request):
    return render(request, 'crypto/game/fase07.html')


def fase08(request):
    return render(request, 'crypto/game/fase08.html')


def fase09(request):
    return render(request, 'crypto/game/fase09.html')


def instrucoes(request):
    return render(request, 'crypto/instrucoes.html')


def embreve(request):
    return render(request, 'crypto/embreve.html')


def ajuda1(request):
    return render(request, 'crypto/ajuda1.html')


def comojogar(request):
    return render(request, 'crypto/comojogar.html')
