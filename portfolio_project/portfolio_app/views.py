from django.shortcuts import render
from .models import *

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def cards(request):
    return render(request, 'cards.html')

def cis(request):
    return render(request, 'cis.html')

def login(request):
    return render(request, 'login form.html')

def register(request):
    return render(request, 'new account.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        text = request.POST['text']
        obj = Contact()
        obj.name = name
        obj.email = email
        obj.text = text
        obj.save()
        return render(request, 'contact.html',{'name': name, 'email': email, 'text':text})
    return render(request, 'contact.html')


