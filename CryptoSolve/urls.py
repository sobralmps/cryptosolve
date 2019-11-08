"""CryptoSolve URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from crypto.views import test1, test2, secret, end, faq, cont
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', test1, name='url_test1'),
    path('menu/', test2, name='url_test2'),
    path('secret/', secret, name='url_secret'),
    path('end/', end, name='url_end'),
    path('faq/', faq, name='url_faq'),
    path('contato/', cont, name='url_cont'),

]
