from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class LavashSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lavash
        fields = '__all__'
        
class CustumersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Custumer
        fields = '__all__'     
        
class KartoshkaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Kartoshka
        fields = '__all__'  
        
class SandvichSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sandvich
        fields = '__all__'     
        
class SalatSerializers(serializers.ModelSerializer):
    class Meta:
        model = Salat
        fields = '__all__'  
        
class IchimliklarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ichimliklar
        fields = '__all__'  
        
class BurgerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Burger
        fields = '__all__'  
        
class HotdogSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hotdog
        fields = '__all__'  
        
class ShirinliklarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Shirinliklar
        fields = '__all__'  