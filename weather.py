import requests

def get_weather_data(location):
    # Use the OpenWeatherMap API to retrieve weather data for the specified location
    api_key = "your_api_key"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # Process the data to extract the relevant details
        weather_data = process_weather_data(data)
        return weather_data
    else:
        raise Exception(f"Error: Unable to retrieve weather data for {location}")

def process_weather_data(data):
    # Extract the relevant details from the raw data
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    weather_conditions = data["weather"][0]["description"]

    # Return the processed data as a dictionary
    return {
        "temperature": temperature,
        "humidity": humidity,
        "wind_speed": wind_speed,
        "weather_conditions": weather_conditions
    }