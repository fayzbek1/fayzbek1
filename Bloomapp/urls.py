from django.urls import path
from .views import *

urlpatterns = [

    #Lavash
    path('lavash-list-api',LavashListApiView.as_view()),
    path('lavash-create-api',LavashCreateApi.as_view()),
    path('lavash-update-api/<str:pk>',LavashRetrieveApi.as_view()),
    path('lavash-delete-api/<str:pk>',LavashDestroyApi.as_view()),

    #Burger
    path('burger-list-api',BurgerListApiView.as_view()),
    path('burger-create-api',BurgerCreateApi.as_view()),
    path('burger-update-api/<str:pk>',BurgerRetrieveApi.as_view()),
    path('burger-delete-api/<str:pk>',BurgerDestroyApi.as_view()),

    #Salat
    path('salat-list-api',SalatListApiView.as_view()),
    path('salat-create-api',SalatCreateApi.as_view()),
    path('salat-update-api/<str:pk>',SalatRetrieveApi.as_view()),
    path('salat-delete-api/<str:pk>',SalatDestroyApi.as_view()),

    #Sandvich
    path('sandvich-list-api',SandvichListApiView.as_view()),
    path('sandvich-create-api',SandvichCreateApi.as_view()),
    path('sandvich-update-api/<str:pk>',SandvichRetrieveApi.as_view()),
    path('sandvich-delete-api/<str:pk>',SandvichDestroyApi.as_view()),

    #Hotdog
    path('hotdog-list-api',HotdogListApiView.as_view()),
    path('hotdog-create-api',HotdogCreateApi.as_view()),
    path('hotdog-update-api/<str:pk>',HotdogRetrieveApi.as_view()),
    path('hotdog-delete-api/<str:pk>',HotdogDestroyApi.as_view()),

    #Kartoshka
    path('kartoshka-list-api',KartoshkaListApiView.as_view()),
    path('kartoshka-create-api',KartoshkaCreateApi.as_view()),
    path('kartoshka-update-api/<str:pk>',KartoshkaRetrieveApi.as_view()),
    path('kartoshka-delete-api/<str:pk>',KartoshkaCreateApi.as_view()),

    #Ichimlik
    path('ichimlik-list-api',IchimlikListApiView.as_view()),
    path('ichimlik-create-api',IchimlikCreateApi.as_view()),
    path('ichimlik-update-api/<str:pk>',IchimlikRetrieveApi.as_view()),
    path('ichimlik-delete-api/<str:pk>',IchimlikDestroyApi.as_view()),

    #Shirinlik
    path('shirinlik-list-api',ShirinlikListApiView.as_view()),
    path('shirinlik-create-api',ShirinlikCreateApi.as_view()),
    path('shirinlik-udpate-api/<str:pk>',ShirinlikRetrieveApi.as_view()),
    path('shirinlik-delete-api/<str:pk>',ShirinlikDestroyApi.as_view()),

    #Customers
    path('customer-crud-api/<str:pk>',CustomerCRUDApi.as_view()),
    #sale

]

