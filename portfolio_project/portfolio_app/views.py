from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

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
        form = contact_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = contact_form()

    return render(request, 'contact.html', {'form': form})


def view_image(request):
    if request.method == 'POST':
        form =ImageForms( data = request.POST, files = request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = ImageForms()
    return render(request,'img.html',{'form':form})    

def update_review(request, id):
    update = get_object_or_404(Img,pk = id)
    if request.method == 'POST':
        form = ImageForms(request.POST, request.FILES, instance = update)
        if form.is_valid():
            form.save()
            update.save()
            return redirect('home')
    return render(request, 'update.html',{'update':update})

def delete_review(request, id):
    instance = get_object_or_404(Img, pk =id)
    instance.profile.delete(save = True)
    instance.delete()
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