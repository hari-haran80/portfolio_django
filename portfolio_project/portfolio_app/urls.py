from django.contrib import admin
from django.urls import path, re_path
from . import views
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.IMAGE_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
  
    path('', views.home, name = 'home'),
    path('home', views.home, name = 'home'),
    path('about', views.about, name = 'about'),
    path('resume/', views.resume_view, name='resume'),
    
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
    path('Confirm_Profile_delete/<int:id>', views.Confirm_Profile_delete, name = 'Confirm_Profile_delete'),
    path('Delete_profile/<int:id>', views.Delete_profile, name='Delete_profile'),
    
    # **************** User Review Section ********************
    # Create Review Section is with Home page Views
    
    path('update/<int:id>/', views.update_review, name='update_review'),
    path('del_data/<int:id>', views.delete_review, name='delete data'),
    path('Confirm-delete/<int:id>', views.Confirm_delete, name = 'Confirm-delete'),
    
    # ***************** Access Denied *****************

    path('AccessDenied', views.Denied, name = 'Denied')
]