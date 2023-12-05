from check import run_check
from locationService import get_current_location
from getForecast import get_weekly_average_forecast
import datetime

class WeatherDay:
    def __init__(self, day, temperature_day, temperature_night):
        """
        Represents a day in the weekly weather forecast.
        Parameters:
        - day (datetime.date): The date of the forecast.
        - temperature_day (float): The daytime temperature.
        - temperature_night (float): The nighttime temperature.
        """
        self.day = day
        self.temperature_day = temperature_day
        self.temperature_night = temperature_night

    def __str__(self):
        """
        Returns a string representation of the WeatherDay object.
        Returns:
        - str: A formatted string containing date, daytime temperature, and nighttime temperature.
        """
        return f"{self.day.strftime('%m/%d/%Y')}: Day - {self.temperature_day}, Night - {self.temperature_night}"

def print_weekly_average(weekly_average):
    """
    Print the weekly weather average.

    Parameters:
    - weekly_average (list): List of weather forecast data.

    Returns:
    - None
    """
    for day in weekly_average:
        print("---------")
        print(f"Day {day.name}")
        print(f"Temperature {day.temperature}")

def _create_weekly_average_weather_(weekly_average):
    """
    Create a list of WeatherDay objects from weekly weather forecast data.

    Parameters:
    - weekly_average (list): List of weather forecast data.

    Returns:
    - list: List of WeatherDay objects representing the weekly forecast.
    """
    weekly_average_weather = []
    current_date = datetime.date.today()

    for i in range(0, len(weekly_average), 2):
        if (weekly_average[i + 1] != 'Tonight'):
            weekly_average_weather.append(WeatherDay(current_date, None, weekly_average[i]))
        else:
            day1_day_temperatures = weekly_average[i]
            day1_night_temperatures = weekly_average[i + 1]
            
            weekly_average_weather.append(WeatherDay(current_date, day1_day_temperatures, day1_night_temperatures))
            current_date += datetime.timedelta(days=1)

    return weekly_average_weather

def get_weekly_average():
    latitude, longitude = get_current_location()
    weekly_average = get_weekly_average_forecast(latitude, longitude)
    return weekly_average

def update():
    """
    Update the weekly weather forecast.

    Returns:
    - list: List of WeatherDay objects representing the updated weekly forecast.
    """
    if run_check():
        print("Access Available")
    else:
        print("Checks failed. Exiting.")
        return

    weekly_average_weather = _create_weekly_average_weather_(get_weekly_average())
    return weekly_average_weather

#if __name__ == "__main__":
    #update()
