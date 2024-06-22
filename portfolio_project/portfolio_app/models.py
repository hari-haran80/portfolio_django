from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.templatetags.static import static
from django.dispatch import receiver
from django.db.models.signals import post_save

class Contact(models.Model):
    
    web_choice = [
        ('Front End', 'Front End'),
        ('Back End', 'Back End'),
        ('Full Stack Website', 'Full Stack Website'),
        ("I'm not sure yet", "I'm not sure yet"),
    ]
        
        
    days_choice = [
        ('2 - 4 weeks', '2 - 4 weeks'),
        ('1 - 2 Months', '1 - 2 Months'),
        ('More than 2 months', 'More than 2 months'),
    ]
    
    name = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 50)
    web = models.CharField(choices=web_choice, max_length = 50, null = True, blank = True)
    days = models.CharField(choices=days_choice,max_length = 50, null = True, blank = True)
    text = models.TextField(max_length = 500)
    
    def __str__(self):
        return self.name.upper()
    
    
class UserProfile(models.Model):
    Gender_choices = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    pro = models.OneToOneField(User, on_delete=models.CASCADE, default=None, null=True, blank=True)
    position = models.CharField(max_length=50, default="Select Profession", null=True, blank=True)
    profile = models.ImageField(upload_to="static/profile", max_length=100, default=static("images/profileimage.png"), null=True, blank=True)
    gender = models.CharField(choices=Gender_choices, max_length=6, default=None, null=True, blank=True)
    mobile = PhoneNumberField(null=False, blank=False, default='+91')

    def __str__(self):
        return str(self.pro.username)
    
    @receiver(post_save, sender=User)
    def create_or_update_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(pro=instance)
        else:
            instance.userprofile.save()
    
class UserReview(models.Model):
    
    profile_name = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    rating = models.IntegerField(default = 0)
    review = models.CharField(max_length = 2000)
    
    def __str__(self):
        return str(self.profile_name.pro.username)+"'s Review"
    
    
class GalleryCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='static/Galary/', blank=True, null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    gallery_category = models.ForeignKey(GalleryCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/Galary/', blank=True, null=True)

    def __str__(self):
        return self.name