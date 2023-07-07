import requests
import os
from dotenv import load_dotenv

class Weather():
    def __init__(self):
        load_dotenv()
        self.key = os.getenv('WEATHER_API_KEY')
        
    def get(self, city):
        response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={self.key}&q={city}&aqi=no")
        if response.status_code == 200:
            print("Todo bien! Respuesta:")
            print(response.json())
            result = {}
            result["temperatura"] = str(response.json()["current"]["temp_c"]) + " grados celsius"
            result["condicion"] = response.json()["current"]["condition"]["text"]
            return result
            #return response.json()
        else:
            print(f"Oops, algo salió mal al llamar al API del clima. Codigo fue: {response.status_code}")