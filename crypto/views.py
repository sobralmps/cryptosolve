from django.shortcuts import render, redirect

def test1(request):
    return render(request, 'crypto/test1.html')