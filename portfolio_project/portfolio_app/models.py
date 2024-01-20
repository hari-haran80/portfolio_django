from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 50)
    text = models.TextField(max_length = 500)
    
    
class Img(models.Model):
    name = models.CharField(max_length = 50)
    position = models.CharField(max_length =50)
    write_review = models.TextField(max_length =1000)
    profile = models.ImageField(upload_to="images", max_length = 100)
    