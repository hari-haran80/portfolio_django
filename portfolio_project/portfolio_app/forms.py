from django import forms
from .models import Img

class ImageForms(forms.ModelForm):
    class Meta:
        model = Img
        fields = "__all__"
        