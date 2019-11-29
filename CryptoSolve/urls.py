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
from crypto.views import homepage, menu, endgame, congrats, faq, cont
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='url_home'),
    path('menu/', menu, name='url_menu'),
    path('congrats/', congrats, name='url_congrats'),
    path('endgame/', endgame, name='url_endgame'),
    path('faq/', faq, name='url_faq'),
    path('contato/', cont, name='url_cont'),

]
