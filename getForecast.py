import requests

class DailyForecast:
    def __init__(self, forecast_data):
        self.start_time = forecast_data.get("startTime")
        self.end_time = forecast_data.get("endTime")
        self.is_daytime = forecast_data.get("isDaytime")
        self.temperature = forecast_data.get("temperature")
        self.temperature_unit = forecast_data.get("temperatureUnit")
        self.temperature_trend = forecast_data.get("temperatureTrend", None)
        self.probability_of_precipitation = forecast_data.get("probabilityOfPrecipitation", {}).get("value")
        self.dewpoint = forecast_data.get("dewpoint", {}).get("value")
        self.relative_humidity = forecast_data.get("relativeHumidity", {}).get("value")
        self.wind_speed = forecast_data.get("windSpeed")
        self.wind_direction = forecast_data.get("windDirection")
        self.icon_url = forecast_data.get("icon")
        self.short_forecast = forecast_data.get("shortForecast")
        self.detailed_forecast = forecast_data.get("detailedForecast")

def get_weekly_average_forecast(lat, lon):
    """
    Get the weekly average forecast for a given location.

    Parameters:
    - lat (float): Latitude of the location.
    - lon (float): Longitude of the location.

    Returns:
    - list: List of DailyForecast objects representing the forecast for each day.
    """
    points_url = f"https://api.weather.gov/points/{lat},{lon}"
    response_points = requests.get(points_url)

    if response_points.status_code != 200:
        raise requests.RequestException(f"Error fetching /points data. Status code: {response_points.status_code}")

    try:
        points_data = response_points.json()

        if "forecast" not in points_data["properties"]:
            raise ValueError("Error: Forecast URL not found in /points endpoint.")

        forecast_url = points_data["properties"]["forecast"] 
        response_forecast = requests.get(forecast_url)

        if response_forecast.status_code != 200:
            raise requests.RequestException(f"Error fetching forecast data. Status code: {response_forecast.status_code}")

        forecast_data = response_forecast.json()
        daily_forecast_array = [DailyForecast(period) for period in forecast_data["properties"]["periods"]]

        return daily_forecast_array

    except ValueError as e:
        raise ValueError(f"Error parsing JSON: {e}")
