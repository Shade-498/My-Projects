import requests

API_KEY = "06405440a3f94ed5bca92516251203"

def get_weather(city):
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
    response = requests.get(url)

    if response.status_code == 200: # Check if the request was successful
        data = response.json()

        weather = data['current']['condition']['text'] # Weather description
        temperature = data['current']['temp_c'] # Temperature in Celsius
        humidity = data['current']['humidity'] # Humidity
        wind_speed = data['current']['wind_kph'] # Wind speed in km/h

        # Print the weather information
        print(f"Weather in {city}: {weather}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed}km/h")

    else:
        print("Error fetching weather data.") # Error message


def main():
    while True:
        city = input("Enter a city name: ")
        get_weather(city)
        print('='*30) # Divider


if __name__ == "__main__":
    main()