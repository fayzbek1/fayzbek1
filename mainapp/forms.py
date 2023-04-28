from django import forms
from .models import *

class CreationFoodtitleForm(forms.ModelForm):
    class Meta:
        model = Food_title
        fields = ['title']
        
class CreationFoodsForm(forms.ModelForm):
    class Meta:
        model = Foods
        fields = ['title','food','decsruction','price','image','quontity',]
        
class CreationCustumerForm(forms.ModelForm):
    class Meta:
        model = Custumer
        fields = ['full_name','adress','gender',]
        
class CreationNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['about',]
        
class CreationCartProductForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['products']        