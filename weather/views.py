from django.shortcuts import render
from .models import City
import requests
from .forms import CityForm

def index(request):
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=c0df7a91296a805430a274a4fba68a82'

	city = 'Philadelphia'

	if request.method == 'POST':
		form = CityForm(request.POST)
		form.save()


	form = CityForm()

	cities = City.objects.all()

	data = []

	for city in cities:
		r = requests.get(url.format(city)).json()

		city_weather = {
			'city': city.name,
			'temperature': r['main']['temp'],
			'description': r['weather'][0]['description'],
			'icon': r['weather'][0]['icon'],
		}

		data.append(city_weather)

	context = {'data': data, 'form': form}
	return render(request, 'weather/weather.html', context)
