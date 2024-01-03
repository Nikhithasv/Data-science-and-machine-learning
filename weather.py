import requests #requests==2.28.1
import json

def get_weather(city):
    api_key = "2544438d8133d808f69b0ea4c589c43a"
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    try:
        url = f"{base_url}?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperature = data["main"]["temp"]
            description = data["weather"][0]["description"]
            print(f"Weather in {city}:")
            print(f"Temperature: {temperature}°C")
            print(f"Description: {description}")
        else:
            print("Failed to retrieve weather data. Please try again.")

    except requests.exceptions.RequestException as e:
        print("Error occurred while retrieving weather data:", e)
city = input("Enter a city name: ")
get_weather(city)
