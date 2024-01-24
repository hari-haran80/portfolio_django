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
            return redirect('home')
    form = ImageForms()
    return render(request,'img.html',{'form':form})    

def update_review(request, id):
    update = Img.objects.get(pk = id)
    if request.method == 'POST':
        name = request.POST['name']
        position = request.POST['position']
        write_review = request.POST['write_review']
        update.name = name
        update.position = position
        update.write_review = write_review
        update.save()
        return redirect('home')
    return render(request, 'update.html',{'update':update})

def delete_review(request, id):
    data = Img.objects.get(pk = id)
    data.delete()
    return redirect('home')


def Login_new(request):
    return render(request, 'signin.html')

def register_new(request):
    if request.method == 'POST':
        Fname = request.POST['Fname']
        Lname = request.POST['Lname']
        Email = request.POST['Email']
        Password = request.POST['Password']
        Mobile = request.POST['Mobile']
        data1 = Register()
        data1.Fname = Fname
        data1.Lname = Lname
        data1.Email = Email
        data1.Password = Password
        data1.Mobile = Mobile
        data1.save()
        return redirect('signin.html')
    return render(request, 'register.html')