from check import run_check
from locationService import get_current_location
from getForecast import get_weekly_average_forecast

if run_check():
    print("Access Available")
else:
    print("Checks failed. Exiting.")

latitude, longitude = get_current_location()
weekly_average = get_weekly_average_forecast(latitude, longitude)





for day in weekly_average:
    print(day.temperature)
print(weekly_average)