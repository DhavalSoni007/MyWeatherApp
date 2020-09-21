import requests
import configparser
from flask import Flask, render_template, request


def get_weather_results(city_name, api_key):

#    country_code= "91" 
   api_url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(city_name, api_key)
   r = requests.get(api_url)
   return r.json()

#    print(api_url)

def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']


# print(get_weather_results("95129", get_api_key()))


app = Flask(__name__)

@app.route('/')
def weather_dashboard():
    # Location= request.form["city_name"]
    return render_template('home.html')

@app.route('/Weather_at', methods={'POST'})

def render_results():
    Cityname= request.form["city_name"]
    data= get_weather_results(Cityname, get_api_key())
    temperature = "{0:.2f}".format(data["main"]["temp"])
    min_temp = "{0:.2f}".format(data["main"]["temp_min"])
    max_temp = "{0:.2f}".format(data["main"]["temp_max"])
    pressure = data["main"]["pressure"]
    humidity = data["main"]["humidity"]
    visibility = data["visibility"]
    wind_speed = data["wind"]["speed"]
    wind_degree = data["wind"]["deg"]
    clouds = data["clouds"]["all"]
    feels_like = "{0:.2f}".format(data["main"]["feels_like"])
    weather= data["weather"][0]["main"]
    location = data["name"]
    return render_template("result.html", temperature=temperature, weather=weather, location=location, min_temp=min_temp, max_temp=max_temp, pressure=pressure, humidity=humidity, visibility=visibility, wind_speed=wind_speed, wind_degree=wind_degree, clouds=clouds, feels_like=feels_like)
if __name__ == '__main__':
    app.run()





