from django.db import models
from djmoney.models.fields import MoneyField

GENDER = [
    
    ('male','male'),
    ('fmale','famale'),

    

]

#class Foods(models.Model):
#    title = models.CharField(max_length=50, choices=GENDER, default='burger')
#    food = models.CharField(max_length=100)
#    about_food = models.TextField()
#    price = MoneyField(max_digits=5,decimal_places=0,default_currency='USD')   #Uzbekistani Som

#    image = models.ImageField(upload_to='foods')
    
#    def __str__(self):
#        return self.food 

class Lavash(models.Model):
    title = models.CharField(max_length=500)
    decsruction = models.TextField()
    price = MoneyField(max_digits=5,decimal_places=0,default_currency='Uzbekistani Som')   #Uzbekistani Som
    image = models.ImageField(upload_to='foods')
    
    def __str__(self):
        return self.title        

class Burger(models.Model):
    title = models.CharField(max_length=500)
    decsruction = models.TextField()
    price = MoneyField(max_digits=5,decimal_places=0,default_currency='Uzbekistani Som')   #Uzbekistani Som
    image = models.ImageField(upload_to='foods')
    
    def __str__(self):
        return self.title    
    
class Salat(models.Model):
    title = models.CharField(max_length=500)
    decsruction = models.TextField()
    price = MoneyField(max_digits=5,decimal_places=0,default_currency='Uzbekistani Som')   #Uzbekistani Som
    image = models.ImageField(upload_to='foods')
    
    def __str__(self):
        return self.title    
    
class Sandvich(models.Model):
    title = models.CharField(max_length=500)
    decsruction = models.TextField()
    price = MoneyField(max_digits=5,decimal_places=0,default_currency='Uzbekistani Som')   #Uzbekistani Som
    image = models.ImageField(upload_to='foods')
    
    def __str__(self):
        return self.title   
    
class Hotdog(models.Model):
    title = models.CharField(max_length=500)
    decsruction = models.TextField()
    price = MoneyField(max_digits=5,decimal_places=0,default_currency='Uzbekistani Som')   #Uzbekistani Som
    image = models.ImageField(upload_to='foods')
    
    def __str__(self):
        return self.title      
    
class Kartoshka(models.Model):
    title = models.CharField(max_length=500)
    decsruction = models.TextField()
    price = MoneyField(max_digits=5,decimal_places=0,default_currency='Uzbekistani Som')   #Uzbekistani Som
    image = models.ImageField(upload_to='foods')
    
    def __str__(self):
        return self.title                   

class Ichimliklar(models.Model):
    title = models.CharField(max_length=500)
    decsruction = models.TextField()
    price = MoneyField(max_digits=5,decimal_places=0,default_currency='Uzbekistani Som')   #Uzbekistani Som
    image = models.ImageField(upload_to='foods')
    
    def __str__(self):
        return self.title    
    
    
class Shirinliklar(models.Model):
    title = models.CharField(max_length=500)
    decsruction = models.TextField()
    price = MoneyField(max_digits=5,decimal_places=0,default_currency='Uzbekistani Som')   #Uzbekistani Som
    image = models.ImageField(upload_to='foods')
    
    def __str__(self):
        return self.title    
       

class Custumer(models.Model):
    full_name = models.CharField(max_length=100)
    adress = models.CharField(max_length=700)
    gender = models.CharField(max_length=50, choices=GENDER, default='burger')
    
    
    def __str__(self):
        return self.full_name