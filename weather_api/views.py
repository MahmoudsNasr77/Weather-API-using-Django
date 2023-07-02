from django.http import HttpResponse
from django.shortcuts import render
from . models import city_info

import requests
# Create your views here.
api_url="http://api.openweathermap.org./data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q="
def index(request):
    if request.method=='POST':
            city="cairo"
            city=request.POST['city']
            url=api_url+city
            response=requests.get(url)
            context=response.json()

            city_wheather={
            'city':city,
            'temperature':int((context['main']['temp'])-273.15),
            'contery':context['sys']['country'],
            'description':context['weather'][0]['description'],
            }
            c=city_info(city=city_wheather['city'],contery=city_wheather['contery'],
                      temperature=city_wheather['temperature'],decription=city_wheather['description'])
            c.save()
            return render(request,'wheather.html',{'city':city_wheather})    
    return render(request,'wheather.html')


