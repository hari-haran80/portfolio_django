from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.urls import reverse

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

#-------------- Review section --------------

@login_required(login_url='signin.html')
def view_image(request):

    if request.method == 'POST':
        form =ImageForms( data = request.POST, files = request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home')
    form = ImageForms()

    return render(request,'img.html',{'form':form})    

@login_required(login_url='signin.html')
def update_review(request, id):
    update = get_object_or_404(Img,pk = id)

    if request.method == 'POST':
        form = ImageForms(request.POST, request.FILES, instance = update)

        if form.is_valid():
            form.save()
            update.save()
            return redirect('home')

    return render(request, 'update.html',{'update':update})


@login_required(login_url='signin.html')
def delete_review(request, id):

    instance = get_object_or_404(Img, pk =id)
    instance.profile.delete(save = True)
    instance.delete()

    return redirect('home')


# ---------------- Create User Account --------------------------

def register_new(request):

    if request.method == 'POST':
        username = request.POST['username']
        First_name = request.POST['First_name']
        Last_name = request.POST['Last_name']
        email = request.POST['email']
        Password1 = request.POST['Password1']
        Password2 = request.POST['Password2']
        
        if Password1 == Password2:
            data1 = User.objects.create_user(
            username=username,
            first_name=First_name,
            last_name=Last_name,
            email=email,
            password=Password1
        )
            data1.is_staff = True
            data1.save()
            data1.set_password(Password1)
            messages.success(request, 'account has created successfully')
            return redirect('/signin')
            
        else:
            messages.error(request, 'password do not match')
            return render(request, 'register.html')
       
    
    return render(request, 'register.html')


# ----------- user profile ----------------------

@login_required(login_url='signin.html')
def User_profile(request, id):
    
    user = user_about.objects.get(pro_id = id)
    user1 = user.pro 
    
    context = {
        
        'user_datas' : user, 
        'user1':user1
        
    }
    
    return render(request, 'profile.html', context)

# ---------- update user profile ------------------------

def update_profile(request, id):
    
    update = user_about.objects.get(pro_id = id)
    
    if request.method =="POST":
        update.profile1 = request.FILES['profile1']
        update.gender1 = request.POST['gender1']
        update.mobile1 = request.POST['mobile1']
        update.position1 = request.POST['position1']
        update.pro.user.username = request.POST['username']
        update.pro.user.first_name = request.POST['first_name']
        update.pro.user.last_name = request.POST['last_name']
        update.pro.user.email = request.POST['email']
        update.pro.user.save()
        update.save()
        
        return redirect(reverse('profile', kwargs={'id': id}))
    
    return render(request, 'update_profile.html',{'update':update})
        
# ------------------- LogIn section ----------------------
def Login_new(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)

        if user is not None:
            auth_login (request, user)
            return redirect('home')
        
        else:
            messages.error(request, 'enter correct username and password')
            return render(request, 'signin.html')
        
    return render(request, 'signin.html')

# ------------------- LogOut section --------------------

@login_required(login_url='signin.html')
def logout_user(request):
    logout(request)

    return redirect('signin')

# ----------------- Forget Password ----------------------

def reset_password(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user = get_user_model().objects.get(username =username)
        
        except:
            messages.warning(request,'User does not exist!')
            return render (request, 'forget.html')
        
        user.set_password(password)
        user.save()
        
        messages.success(request, 'password reset successfully')
        return redirect('signin')  
          
    return render (request, 'forget.html')

