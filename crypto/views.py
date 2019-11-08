from django.shortcuts import render, redirect


def test1(request):
    return render(request, 'crypto/test1.html')


def test2(request):
    return render(request, 'crypto/test2.html')


def secret(request):
    return render(request, 'crypto/secret.html')


def end(request):
    return render(request, 'crypto/end.html')

def faq(request):
    return render(request, 'crypto/faq.html')

def cont(request):
    return render(request, 'crypto/contato.html')
