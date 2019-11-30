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
from crypto import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='url_home'),
    path('menu/', views.menu, name='url_menu'),
    path('congrats/', views.congrats, name='url_congrats'),
    path('game/wqb/', views.fim, name='url_fim'),
    path('faq/', views.faq, name='url_faq'),
    path('contato/', views.cont, name='url_cont'),
    path('game/wd/', views.fase01, name='url_fase01'),
    path('game/ldbg/', views.fase02, name='url_fase02'),
    path('game/ziex/', views.fase03, name='url_fase03'),
    path('game/yuckzd/', views.fase04, name='url_fase04'),
    path('game/vwtto/', views.fase05, name='url_fase05'),
    path('game/xmiu/', views.fase06, name='url_fase06'),
    path('game/jmix/', views.fase07, name='url_fase07'),
    path('game/coko/', views.fase08, name='url_fase08'),
    path('game/swvg/', views.fase09, name='url_fase09'),
    path('instrucoes/', views.instrucoes, name='url_instrucoes'),
    path('embreve/', views.embreve, name='url_embreve'),
    path('ajuda1/', views.ajuda1, name='url_ajuda1'),
    path('comojogar/', views.comojogar, name='url_comojogar'),
]
