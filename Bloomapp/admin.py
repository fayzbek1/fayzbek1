from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Lavash)
admin.site.register(Kartoshka)
admin.site.register(Sandvich)
admin.site.register(Salat)
admin.site.register(Ichimliklar)
admin.site.register(Burger)
admin.site.register(Hotdog)
admin.site.register(Shirinliklar)

#custumer
admin.site.register(Custumer)