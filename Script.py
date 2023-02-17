import requests
import json
import subprocess


# Your OpenWeather API key and location
api_key = ""
lat = ""
lon = ""


def get_weather(api_key, lat, lon):
    # Use OpenWeather API to get weather data
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    weather_data = requests.get(weather_url).json()
    return weather_data["weather"][0]["main"].lower()


def get_image(weather_tag):
    # Use e621 API to get image data
    image_url = f"https://e621.net/posts.json?tags={weather_tag}+score:>250+16:9+-animated&limit=1&random=true"
    image_data = requests.get(image_url, headers = {'user-agent' : 'i3 background /1.0 (by sebek4321)'}).json()
    return image_data["posts"][0]["file"]["url"]


def change_background(api_key, lat, lon):
    # Get the current weather
    weather = get_weather(api_key, lat, lon)
    # Declare the tag
    weather_tag = "outside"


    # Determine the weather tag to use
    if weather == "clear":
        weather_tag = "blue_sky"
    elif weather == "clouds":
        weather_tag = "cloud"
    elif weather == "rain":
        weather_tag = "raining"
    elif weather == "snow":
        weather_tag = "snow"
    elif weather == "thunderstorm":
        weather_tag = "raining+lightning"
    elif weather == "drizzle":
        weather_tag = "rain"
    elif weather == "fog":
        weather_tag = "fog"
    elif weather == "mist":
        weather_tag = "rain"
    else:
        weather_tag = "outside"


    # Get the image URL
    image_url = get_image(weather_tag)
    print(image_url)
    # Set the background using the i3 "feh" command
    set_background_command = f"feh --bg-fill {image_url}"
    subprocess.run(set_background_command.split(), check=True)



# For testing
print(get_weather(api_key, lat, lon))


# Change the background
change_background(api_key, lat, lon)
