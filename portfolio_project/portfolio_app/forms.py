from django import forms
from .models import Contact, UserProfile, UserReview
from django.contrib.auth.models import User

class ImageForms(forms.ModelForm):
    class Meta:
        model = UserReview
        fields = "__all__"
        widgets = {
            'review': forms.Textarea(attrs={'rows': 7, 'cols': 36}),
        }
        
        
class contact_form(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'web', 'days', 'text']
        
        
        
class update_profile_form(forms.ModelForm):
    class Mete:
        model = User
        fields =  ["username", "email", " first_name","last_name"]
        
        
class AddProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["pro","position","gender","mobile"]