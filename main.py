#Code Tkinter Frontend Here
from weather_backend import *

# Update the weekly weather forecast
weekly_weather = update()

# Example 1: Accessing WeatherDay properties with conditions weekly_weather contains both a day and night class inside
day_one = weekly_weather[0]

#print(day_one.temperature_day.get_name()) cant get it since its night time so its None type so add in a if statement if day_one temperature_day is None then skip 
# Check if temperature_day is None before accessing its properties
if day_one.temperature_day is not None:
    print(f"Day One (Daytime): {day_one.temperature_day.get_name()}")
else:
    print("Day One (Nighttime): Skipped due to nighttime forecast")


#-----------------------------------------------#


# accesing more of the raw data by calling this total of 14 days and nights combined
weekly_weather = get_weekly_average()

print(weekly_weather[0].get_name())
print(weekly_weather[1].get_name())
print(weekly_weather[2].get_name())
print(weekly_weather[3].get_name())
print(weekly_weather[4].get_name())
print(weekly_weather[5].get_name())
print(weekly_weather[6].get_name())
print(weekly_weather[7].get_name())
print(weekly_weather[8].get_name())
print(weekly_weather[9].get_name())
print(weekly_weather[10].get_name())
print(weekly_weather[11].get_name())
print(weekly_weather[12].get_name())
print(weekly_weather[13].get_name())


