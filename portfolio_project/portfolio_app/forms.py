from django import forms
from .models import Contact, Img, profile
from django.contrib.auth.models import User

class ImageForms(forms.ModelForm):
    class Meta:
        model = Img
        fields = "__all__"
        
        
class contact_form(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'web', 'days', 'text']
        
        
        
class profile_form(forms.ModelForm):
    
    class Meta:
        model = profile
        fields = '__all__'
        
        
class update_profile_form(forms.ModelForm):
    class Mete:
        model = User
        fields =  ["username", "email", " first_name","last_name"]
        