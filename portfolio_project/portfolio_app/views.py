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
    
    user_profile = UserProfile.objects.get(pro=request.user)
    user_review = UserReview.objects.filter(profile_name=user_profile).exists()
    
    # Write Review Section
    
    if request.method == 'POST':
        rating = request.POST.get('rating')
        review_text = request.POST.get('review')
        
        profile = UserProfile.objects.get(pro=request.user)
        
        if UserReview.objects.filter(profile_name=profile).exists():
            messages.error(request, 'You have already submitted a review.')
        else:
            UserReview.objects.create(
                profile_name=profile,
                rating=rating,
                review=review_text
            )
            messages.success(request, 'Your review has been submitted successfully.')
            return redirect('home')

    context = {
        'image':data,
        'profile':profile,
        'user_review': user_review
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

def delete_contact(request,id):
    instance = get_object_or_404(Contact, pk =id)
    instance.delete()
    return redirect('view_contact')

# ------------- Review Section ----------------

@login_required(login_url='signin')
def update_review(request, id):
    
    reviews = UserReview.objects.get(pk = id)
    
    if request.method == "POST":
    
        reviews.rating = request.POST['rating']
        reviews.review = request.POST['review']
        reviews.save()
    
        response = HttpResponse('<script>window.parent.closeAndUpdate();</script>')
        messages.success(request, 'Your review Updated successfully.')
        return response
    
    return render (request, 'Review_update.html',{'reviews':reviews})


@login_required(login_url='signin')
def delete_review(request, id):

    instance = get_object_or_404(UserReview, pk =id)
    instance.delete()

    messages.success(request, 'Your review Deleted successfully.')
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
            
            messages.success(request, 'Account Created Successfully!!')
            request.session['username'] = data1.username
            
            return redirect('/signin')
            
        else:
            messages.error(request, 'Password Do Not Match')
            return render(request, 'register.html')
       
    
    return render(request, 'register.html')


# ----------- user profile ----------------------

@login_required(login_url='signin.html')
def User_profile(request, id):
    
    currentUser = request.user.id
    if currentUser != id:
        return render(request, 'access.html')
    
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
    
    currentUser = request.user.id
    if currentUser != id:
        return render(request, 'access.html')
    
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
        
        messages.success(request, 'Profile Updated Successfully')
        return redirect(reverse('profile', kwargs={'id': id}))
    
    return render(request, 'update_profile.html',{'update':update})

# ---------- Delete User Profile ------------------------

def Delete_profile(request, id):
    user = request.user
    user.delete()
    return redirect('signin')
        
# ------------------- LogIn section ----------------------

def Login_new(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)

        if user is not None:
            auth_login (request, user)
            messages.success(request, 'Welcome Back '+ user.first_name)
            return redirect('home')
        
        else:
            messages.error(request, 'Enter Correct Username and Password')
            return render(request, 'signin.html')
        
    return render(request, 'signin.html')

# ------------------- LogOut section --------------------

@login_required(login_url='signin.html')
def logout_user(request):
    logout(request)

    messages.success(request, 'We hope to see you again soon! 😊')
    request.session.flush()
    return redirect('signin')

# ----------------- Forget Password ----------------------

def reset_password(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user = get_user_model().objects.get(username =username)
        
        except:
            messages.warning(request,'User Does Not Exist!')
            return render (request, 'forget.html')
        
        user.set_password(password)
        user.save()
        
        messages.success(request, 'Password Reset Successfully')
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

# ******************** Access and Error Section ***********************

def Denied(request):
    return render(request, 'access.html')

def custom_page_not_found(request, exception):
    return render(request, 'error.html', status=404)