from django.db import models

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
    name = models.CharField(max_length = 50)
    position = models.CharField(max_length =50)
    write_review = models.TextField(max_length =1000)
    profile = models.ImageField(upload_to="images", max_length = 100)
    
    def __str__(self):
        return self.name.upper()