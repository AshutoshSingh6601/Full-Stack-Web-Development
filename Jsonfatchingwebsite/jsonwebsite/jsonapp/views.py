from django.http import HttpResponse
from django.shortcuts import render
from .models import Meals
import requests

# Create your views here.

def home(request):
        response=requests.get('https://www.themealdb.com/api/json/v1/1/search.php?s=%s')
        data=response.json()   
        meals=data['meals']
        for i in meals:
            meal=Meals(slug=i['idMeal'],name=i['strMeal'],category=i['strCategory'],area=i['strArea'],instructions=i['strInstructions'],images=i['strMealThumb'])
            meal.save()

        all_meals=Meals.objects.all()
        context={
            'all_meals':all_meals
        }
        
        return render(request,'home.html',context)


def meal_detail(request,id):
    single_meal=Meals.objects.get(id=id)
    context={
        'single_meal':single_meal,

    }
    return render(request,'meal_detail.html',context)