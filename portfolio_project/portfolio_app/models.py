from django.db import models
from django.contrib.auth.models import User
# from phonenumber_field.modelfields import PhoneNumberField

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
    
    
class Img(models.Model):

    name = models.CharField(max_length = 50, default = '')
    position = models.CharField(max_length =50,default = '')
    write_review = models.TextField(max_length =1000,default = '')
    profile = models.ImageField(upload_to="images", max_length = 100,default = '')
    
    def __str__(self):
        return self.name.upper()
    
    
class User_file(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    
    def __str__(self):
        return  str(self.user.username)
    
    
class user_info(models.Model):
    pro = models.OneToOneField(User_file, on_delete = models.CASCADE)
    review = models.CharField(max_length = 2000)
    
    def __str__(self):
        return  str(self.pro.user.username)
    

class user_about(models.Model):
    
    Gender_choices = [
        ('Male','Male'),
        ('Female', 'Female'),
    ]
     
    pro  = models.OneToOneField(User_file,on_delete = models.CASCADE)
    position1 = models.CharField(max_length = 50)
    profile1 = models.ImageField(upload_to="images", max_length = 100)
    gender1 = models.CharField(choices = Gender_choices, max_length = 6)
    mobile1 = models.IntegerField(null = False, blank = False)
    
    
    def __str__(self):
        return  str(self.pro.user.username)
    