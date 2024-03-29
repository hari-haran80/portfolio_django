from django import forms
from .models import Contact, Img, user_about
from django.contrib.auth.models import User

class ImageForms(forms.ModelForm):
    class Meta:
        model = Img
        fields = "__all__"
        
        
class contact_form(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'web', 'days', 'text']
        
        
        
class update_profile_form(forms.ModelForm):
    class Mete:
        model = User
        fields =  ["username", "email", " first_name","last_name"]
        

class UserAboutForm(forms.ModelForm):
    class Meta:
        model = user_about
        fields = "__all__"