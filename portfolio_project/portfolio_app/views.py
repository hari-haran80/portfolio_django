from django.shortcuts import render, redirect
from .models import *
from .forms import ImageForms

def home(request):
    data = Img.objects.all()
    return render(request, 'index.html',{'image':data})

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


def view_image(request):
    if request.method == 'POST':
        form =ImageForms( data = request.POST, files = request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForms()
    return render(request,'img.html',{'form':form})

