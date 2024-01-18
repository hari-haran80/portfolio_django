from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('index.html', views.home, name = 'home'),
    path('home', views.home, name = 'home'),
    path('about', views.about, name = 'about'),
    path('about.html', views.about, name = 'about'),
    path('cards', views.cards, name = 'cards'),
    path('template/cards.html', views.cards, name = 'cards'),
    path('cis', views.cis, name = 'cis'),
    path('cis.html', views.cis, name = 'cis'),
    path('login', views.login, name = 'login'),
    path('login form.html', views.login, name = 'login'),
    path('register', views.register, name = 'register'),
    path('new account.html', views.register, name = 'register'),
    path('contact', views.contact, name = 'contact'),
    path('contact.html', views.contact, name = 'contact'),
]