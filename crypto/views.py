from django.shortcuts import render, redirect

def test1(request):
    return render(request, 'crypto/test1.html')

def test2(request):
    return render(request, 'crypto/test2.html')

def test3(request):
    return render(request, 'crypto/test3.html')