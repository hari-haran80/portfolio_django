from django import forms
from .models import Contact, Img

class ImageForms(forms.ModelForm):
    class Meta:
        model = Img
        fields = "__all__"
        
        
class contact_form(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'web', 'days', 'text']