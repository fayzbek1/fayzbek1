from django.shortcuts import render,redirect
from .models import *
from .forms import *


# Create your views here.

def index(request):
    #food_title = Food_title.objects.all()
    food = Foods.objects.all()
    context = {
        'food' : food
    }
    return render(request,'mainapp/index.html',context)

def food_title_create(request):
    form = CreationFoodtitleForm()
    if request.method == "POST":
        form = CreationFoodtitleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
        else:
            form = CreationFoodtitleForm()
            
    context = {
        'form' : form
    }
    return render

def food_title_update(request,pk):
    foods_title = Food_title.objects.all(id=pk)
    form = CreationFoodtitleForm(instance=foods_title)
    if request.method == "POST":
        form = CreationFoodtitleForm(request.POST,instance=foods_title)
        if form.is_valid():
            form.save()
            return redirect()
    
    context = {
        'form' : form
    }
    return render()

def food_title_delete(request,pk):
    foods_title = Food_title.objects.get(id=pk)
    if request.method == "POST":
        foods_title.delete()
        return redirect()
    context = {
        'foods_title' : foods_title
    }
    return render()

def foods(request):
    foods = Food_title.objects.all()
    foods = Foods.objects.all()
    context = {
        'foods' : foods
    }
    return render()

def foods_create(request):
    form = CreationFoodsForm()
    if request.method == "POST":
        form = CreationFoodsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
        else:
            form = CreationFoodsForm()
            
    context = {
        'form' : form
    }
    return render

def foods_update(request,pk):
    foods = Foods.objects.all(id=pk)
    form = CreationFoodsForm(instance=foods)
    if request.method == "POST":
        form = CreationFoodsForm(request.POST,instance=foods)
        if form.is_valid():
            form.save()
            return redirect()
    
    context = {
        'form' : form
    }
    return render()

def foods_delete(request,pk):
    foods = Foods.objects.get(id=pk)
    if request.method == "POST":
        foods.delete()
        return redirect()
    context = {
        'foods' : foods
    }
    return render()

def custumer(request):
    custumers = Custumer.objects.all()
    context = {
        'custumers' : custumers
    }
    return render()

def custumer_create(request):
    form = CreationCustumerForm()
    if request.method == "POST":
        form = CreationCustumerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
        else:
            form = CreationCustumerForm()
            
    context = {
        'form' : form
    }
    return render

def custumer_update(request,pk):
    custumers = Custumer.objects.all(id=pk)
    form = CreationCustumerForm(instance=custumers)
    if request.method == "POST":
        form = CreationCustumerForm(request.POST,instance=custumers)
        if form.is_valid():
            form.save()
            return redirect()
    
    context = {
        'form' : form
    }
    return render()

def custumer_delete(request,pk):
    custumers = Custumer.objects.get(id=pk)
    if request.method == "POST":
        custumers.delete()
        return redirect()
    context = {
        'custumers' : custumers
    }
    return render()

def news(request):
    news = News.objects.all()
    context = {
        'news' : news
    }
    return render()

def news_create(request):
    form = CreationNewsForm()
    if request.method == "POST":
        form = CreationNewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
        else:
            form = CreationNewsForm()
            
    context = {
        'form' : form
    }
    return render

def news_update(request,pk):
    news = News.objects.all(id=pk)
    form = CreationNewsForm(instance=news)
    if request.method == "POST":
        form = CreationNewsForm(request.POST,instance=news)
        if form.is_valid():
            form.save()
            return redirect()
    
    context = {
        'form' : form
    }
    return render()

def news_delete(request,pk):
    news = News.objects.get(id=pk)
    if request.method == "POST":
        news.delete()
        return redirect()
    context = {
        'news' : news
    }
    return render()