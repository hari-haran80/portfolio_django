from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 50)
    text = models.TextField(max_length = 500)
    
    def __str__(self, *args, **kwargs):
        return self.name.upper()
    
    
class Img(models.Model):
    name = models.CharField(max_length = 50)
    position = models.CharField(max_length =50)
    write_review = models.TextField(max_length =1000)
    profile = models.ImageField(upload_to="images", max_length = 100)
    
    def __str__(self, *args, **kwargs):
        return self.name.upper()
    
    
class Register(models.Model):
    Fname = models.CharField(max_length = 50)    
    Lname = models.CharField(max_length = 50)    
    Email = models.EmailField(max_length = 100)
    Mobile = models.IntegerField()    
    Password = models.CharField(max_length = 50)    
    
    def __str__(self, *args, **kwargs):
        return self.Fname.upper()