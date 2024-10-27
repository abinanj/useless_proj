import requests
from datetime import datetime, timedelta

# Function to get yesterday's weather
def get_yesterdays_weather(api_key, city):
    # Calculate yesterday's date and create a timestamp for noon
    yesterday = datetime.now() - timedelta(days=1)
    timestamp = int(yesterday.replace(hour=12, minute=0).timestamp())

    # OpenWeatherMap API URL for historical data (replace `lat` and `lon` with actual coordinates for Thrissur)
    url = f"http://api.openweathermap.org/data/2.5/onecall/timemachine?lat=10.5276&lon=76.2144&dt={timestamp}&appid={api_key}&units=metric"

    # Make the API request
    response = requests.get(url)
    data = response.json()

    # Check if the request was successful
    if response.status_code == 200:
        # Extract relevant data
        weather_description = data['current']['weather'][0]['description']
        temperature = data['current']['temp']
        humidity = data['current']['humidity']
        
        # Check if it rained yesterday
        rain_warning = ""
        if "rain" in weather_description.lower():
            rain_warning = "\n\n🌧️ *Ambane, you should carry an umbrella today!* 🌂"

        # Create a funny weather report
        report = f"""
        🌧️ Yesterday's Weather Report for {city} 🌧️
        
        - **Weather**: {weather_description}
        - **Temperature**: {temperature}°C
        - **Humidity**: {humidity}%

        And remember, folks, it rained yesterday! So if you forgot your umbrella, you might as well have taken a swim! 🏊‍♂️
        Don't forget to check your shoes for any fish that might have jumped in! 🐟{rain_warning}
        """

        return report
    else:
        return f"Oops! Couldn't fetch the weather data. Error: {data.get('message', 'Unknown error')}"

# Main function
if __name__ == "__main__":
    API_KEY = "dc83525f07b4485f88a55510242710"  
    CITY = "Thrissur"  

    weather_report = get_yesterdays_weather(API_KEY, CITY)
    print(weather_report)
