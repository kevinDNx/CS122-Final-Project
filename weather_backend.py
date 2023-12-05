
from check import run_check
from locationService import get_current_location
from getForecast import get_weekly_average_forecast
import datetime

class WeatherDay:
    def __init__(self, day, temperature_day, temperature_night):
        self.day = day
        self.temperature_day = temperature_day
        self.temperature_night = temperature_night

    def __str__(self):
        return f"{self.day.strftime('%m/%d/%Y')}: Day - {self.temperature_day}, Night - {self.temperature_night}"

def print_weekly_average(weekly_average):
    for day in weekly_average:
        print("---------")
        print(f"Day {day.name}")
        print(f"Temperature {day.temperature}")

def _create_weekly_average_weather_(weekly_average):
    weekly_average_weather = []
    current_date = datetime.date.today()

    for i in range(0, len(weekly_average), 2):
        day1_day_temperatures = weekly_average[i]
        day1_night_temperatures = weekly_average[i + 1]
        weekly_average_weather.append(WeatherDay(current_date, day1_day_temperatures, day1_night_temperatures))
        current_date += datetime.timedelta(days=1)

    return weekly_average_weather

def update():
    if run_check():
        print("Access Available")
    else:
        print("Checks failed. Exiting.")
        return

    latitude, longitude = get_current_location()
    weekly_average = get_weekly_average_forecast(latitude, longitude)

    weekly_average_weather = _create_weekly_average_weather_(weekly_average)

#if __name__ == "__main__":
    #update()

