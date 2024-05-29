from django import forms
from .models import Contact, UserProfile, UserReview
from django.contrib.auth.models import User

class ImageForms(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        self.user = user
        super(ImageForms, self).__init__(*args, **kwargs)
        if user:
            self.fields['profile_name'].queryset = UserProfile.objects.filter(pro__username=user.username)
            self.fields['profile_name'].initial = UserProfile.objects.get(pro__username=user.username)
            
        self.fields['profile_name'].widget = forms.HiddenInput()

    def save(self, commit=True):
        instance = super(ImageForms, self).save(commit=False)
        if self.user:
            instance.profile_name = UserProfile.objects.get(pro__username=self.user.username)
        if commit:
            instance.save()
        return instance

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
        
        
# class AddProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ["pro","position","gender","mobile"]