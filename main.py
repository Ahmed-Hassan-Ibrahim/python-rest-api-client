import os
import requests

from dataclasses import dataclass
from dotenv import load_dotenv

# Loading enviroment variables=======================================
load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "https://api.weatherapi.com/v1/current.json"
#====================================================================

# Weather Data Class=================================================
@dataclass
class WeatherReport:
    city: str
    country: str
    temperature: float
    humidity: int

    # Method for displaying weather data
    def  display(self):
        print("\n========== WEATHER REPORT ==========")
        print(f"City:           {self.city}, {self.country}")
        print(f"Temperature:    {self.temperature:.1f} °C")
        print(f"Humidity:       {self.humidity}%")
        print("====================================\n")
#====================================================================

# REST API Request and JSON Parsing==================================
def get_weather(city):

    # Check API Key
    if not API_KEY:
        raise ValueError("API key not found! Revise your API key in .env file.")

    # API Request Parameters
    params = {
        "key" : API_KEY,
        "q" : city
    }

    # Send HTTP GET Request
    response = requests.get(BASE_URL, params=params, timeout=10)

    # Check HTTP Response Status
    response.raise_for_status()

    # Parse JSON Response
    data = response.json()

    # Create Object from information in data
    report = WeatherReport(
        city = data["location"]["name"],
        country = data["location"]["country"],
        temperature = data["current"]["temp_c"],
        humidity = data["current"]["humidity"]
    )

    return report
#====================================================================

# Main Program=======================================================
if __name__ == "__main__":
    print("===== Weather Information System =====")

    try:
        # 1) Git city from user
        city = input("Enter city name: ").strip()

        if not city:
            raise ValueError("City name cannot be empty!")

        # 2) Retrieve weather information
        weather = get_weather(city)

        # 3) Display formatted summary
        weather.display()

    # Handles unsuccessful HTTP responses returned by the API
    except requests.exceptions.HTTPError as error:
        print(f"\nAPI error: {error}")

        if error.response is not None:
            try:
                print("Details:", error.response.json()["error"]["messsage"])
            except (ValueError, KeyError):
                pass

    # Handles network-related problems during the HTTP request
    except requests.exceptions.RequestException as error:
        print(f"\nConnection error: {error}")

    # Handles missing keys in the JSON response
    except (KeyError, IndentationError) as error:
        print(f"\nUnexpected API response format: {error}")

    # Handles accessing an invalid list index, invalid configuration, invalid input values
    except ValueError as error:
        print(f"\nConfiguration/Input error: {error}")
#====================================================================