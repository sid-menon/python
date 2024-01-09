# importing requests and json
from calendar import c
from json.tool import main
from re import T
import requests, json

from sklearn.linear_model import TheilSenRegressor
# base URL

def weath(city):
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    CITY = city
    API_KEY = "7604cfbc68735df8a296222c7a2d373d" #7604cfbc68735df8a296222c7a2d373d
    # upadting the URL
    complete_url = BASE_URL + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + CITY
    # HTTP request
    response = requests.get(complete_url)
    # checking the status code of the request
    if response.status_code == 200:
    # getting data in the json format
        data = response.json()
        # getting the main dict block
        main = data['main']
        # getting temperature
        temperature = main['temp'] - 273.15
        # getting the humidity
        humidity = main['humidity']
        # getting the pressure
        pressure = main['pressure']
        # weather report
        report = data['weather']
        weath.temp,dec = divmod(temperature,1)

        str = f"{CITY:-^30}" + "\n" + f"Temperature: {weath.temp}°C"+ "\n" + f"Humidity: {humidity}%" +"\n" + f"Pressure: {pressure} hPa" + "\n" +f"Weather Report: {report[0]['description']}"
        return str
    else:
    # showing the error message
        return "Error in the HTTP request"

def getTemp():
    return weath.temp
