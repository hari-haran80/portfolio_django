from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('home', views.home, name = 'home'),
    path('about', views.about, name = 'about'),
    path('cards', views.cards, name = 'cards'),
    path('cis', views.cis, name = 'cis'),
    path('login', views.login, name = 'login'),
    path('register', views.register, name = 'register'),
    path('contact', views.contact, name = 'contact'),
    path('Write_review', views.view_image, name='Write_review'),
    path('update_data/<int:id>', views.update_review, name='update data'),
    path('del_data/<int:id>', views.delete_review, name='delete data'),
    path('register', views.register_new, name='new_registration'),
    path('signin', views.Login_new, name='signin'),
    path('logout', views.logout_user, name='logout'),
    path('profile/<int:id>', views.User_profile, name='profile'),
    path('profile_update', views.update_profile2, name='profile_update'),
    path('forget_password', views.reset_password, name='forget_password'),
]