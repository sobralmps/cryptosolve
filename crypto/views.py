from django.shortcuts import render, redirect


def test1(request):
    return render(request, 'crypto/test1.html')


def test2(request):
    return render(request, 'crypto/test2.html')


def secret(request):
    return render(request, 'crypto/secret.html')
