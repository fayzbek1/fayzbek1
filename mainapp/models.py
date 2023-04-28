from django.db import models
from djmoney.models.fields import MoneyField

GENDER_CHOICES = [
    
    ('male','male'),
    ('fmale','famale'),

]
class Food_title(models.Model):
    title = models.CharField(max_length=500)
    
    def __str__(self):
        return self.title
        

class Foods(models.Model):
    title = models.ForeignKey(Food_title, on_delete=models.SET_NULL, null=True)
    food = models.CharField(max_length=500)
    decsruction = models.TextField()
    price = MoneyField(max_digits=5,default_currency='Uzbekistani Som')   #Uzbekistani Som
    image = models.ImageField(upload_to='foods')
    quontity = models.IntegerField()
    
    def __str__(self):
        return self.food 
    def total_amounts(self):
        total_amounts = self.price * self.quontity
        return total_amounts

class Custumer(models.Model):
    full_name = models.CharField(max_length=100)
    adress = models.CharField(max_length=700)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, default='male')
    
    
    def __str__(self):
        return self.full_name
    
class News(models.Model):
    about = models.TextField()    
    
    
class Cart(models.Model):
    products = models.ForeignKey(Foods, on_delete=models.SET_NULL, null=True)
    def total_amounts(self):
        total_amounts = self.price * self.quontity
        return total_amounts