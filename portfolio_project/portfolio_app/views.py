from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings


@login_required(login_url='signin')
def home(request):
    data = UserReview.objects.all()
    profile = UserProfile.objects.all()
    if request.method == 'POST':
        form =ImageForms(request.POST, user=request.user)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ImageForms(user=request.user)

    context = {
        'image':data, 
        'form':form,
        'profile':profile
    }
    
    return render(request, 'index.html',context)


@login_required(login_url='signin')
def about(request):
    return render(request, 'about.html')

@login_required(login_url='signin')
def cards(request):
    return render(request, 'cards.html')

@login_required(login_url='signin')
def cis(request):
    return render(request, 'cis.html')

@login_required(login_url='signin')
def login(request):
    return render(request, 'login form.html')

@login_required(login_url='signin')
def register(request):
    return render(request, 'new account.html')

# ----------------- Contact Form section ---------------------- 

@login_required(login_url='signin')
def contact(request):

    if request.method == 'POST':
        form = contact_form(request.POST)

        if form.is_valid():
            form.save()
            
            email = form.cleaned_data['email']
            message = "Thanks for reaching out! We've received your message and will get back to you shortly"
            send_mail(
                'Contact Form Submission',
                message,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False
            )
            messages.success(request, "Your message has been sent successfully! We'll be in touch soon. !!!.")
            return redirect('contact')

    else:
        form = contact_form()

    return render(request, 'contact.html', {'form': form})

def view_contact(request):
    contact = Contact.objects.all()
    return render(request, 'admincontact.html',{'contact':contact})

def delete_contact(id):
    instance = get_object_or_404(Contact, pk =id)
    instance.delete()
    return redirect('view_contact')

# ------------- Review Section ----------------

@login_required(login_url='signin')
def update_review(request, id):
    
    reviews = UserReview.objects.get(pk = id)
    
    if request.method == "POST":
    
        reviews.review = request.POST['review']
        reviews.save()
    
        response = HttpResponse('<script>window.parent.closeAndUpdate();</script>')
        return response
    
    return render (request, 'Review_update.html',{'reviews':reviews})


@login_required(login_url='signin')
def delete_review(request, id):

    instance = get_object_or_404(UserReview, pk =id)
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
            return redirect('/signin')
            
        else:
            messages.error(request, 'password do not match')
            return render(request, 'register.html')
       
    
    return render(request, 'register.html')


# ----------- user profile ----------------------

@login_required(login_url='signin.html')
def User_profile(request, id):
    
    user = UserProfile.objects.get(pro_id = id)
    user1 = user.pro 
    
    context = {
        
        'user_datas' : user, 
        'user1':user1
        
    }
    
    return render(request, 'profile.html', context)

# ---------- update user profile ------------------------

@login_required(login_url='signin')
def update_profile(request, id):
    
    update = UserProfile.objects.get(pro_id = id)
    
    if request.method =="POST":
        update.profile = request.FILES['profile']
        update.gender = request.POST['gender']
        update.mobile = request.POST['mobile']
        update.position = request.POST['position']
        update.pro.username = request.POST['username']
        update.pro.first_name = request.POST['first_name']
        update.pro.last_name = request.POST['last_name']
        update.pro.email = request.POST['email']
        update.pro.save()
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

# ******************** Galary Views Section ***********************

def galary(request):
    
    category = GalleryCategory.objects.all()
    return render(request, 'galary.html',{'category':category})

def Galaryview(request, name):

    images = Category.objects.filter(gallery_category__name=name)    
    context = {
        'images': images,
    }
    
    return render(request, 'viewImage.html', context)


# ********************* Other Unwanted Views Section *********************


# def AddProfile(request):
#     if request.method == 'POST':
#         form = AddProfileForm(data = request.POST, files = request.FILES)
#         if form.is_valid():
#             user_profile = form.save(commit=False)
#             user_profile.save()
#             messages.success(request, 'account has created successfully')
#             return redirect('/signin')
        
#         else:
#             messages.error(request, 'password do not match')
#             return render(request,"addProfile.html")
#     else:
#         form = AddProfileForm()
        
#     return render(request, 'addProfile.html', {'form': form})


# def dummy (request):
#     reviews = UserReview.objects.all()
#     data = UserReview.objects.all()
#     return render(request, 'dummy.html',{'reviews': reviews,'image':data})


# def nav(request):
#     profile = UserProfile.objects.all()
#     return render(request, 'nav.html',{'profile':profile})
