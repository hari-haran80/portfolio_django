from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name = 'home'),
    path('home', views.home, name = 'home'),
    path('about', views.about, name = 'about'),
    
    # **************** Contact Section ********************
   
    path('contact', views.contact, name = 'contact'),
    path('view_contact', views.view_contact, name = 'view_contact'),
    path('delete_contact/<int:id>', views.delete_contact, name = 'delete_contact'),
    
    # **************** Projects Section ********************
    
    path('cards', views.cards, name = 'cards'),
    path('cis', views.cis, name = 'cis'),
    path('gallery', views.galary, name = 'gallery'),
    path('gallery/<str:name>', views.Galaryview, name = 'galary'),
    path('login', views.login, name = 'login'),
    path('register', views.register, name = 'register'),
    
    # **************** User Section ********************
    
    path('new_registration', views.register_new, name='new_registration'),
    path('signin', views.Login_new, name='signin'),
    path('logout', views.logout_user, name='logout'),
    path('forget_password', views.reset_password, name='forget_password'),
    
    # **************** User Profile Section ********************
    
    path('profile/<int:id>', views.User_profile, name='profile'),
    path('profile_update/<int:id>', views.update_profile, name='profile_update'),
    
    # **************** User Review Section ********************
    # Create Review Section is with Home page Views
    
    path('update/<int:id>/', views.update_review, name='update_review'),
    path('del_data/<int:id>', views.delete_review, name='delete data'),
    
    # ***************** Access Denied *****************

    path('AccessDenied', views.Denied, name = 'Denied')
]