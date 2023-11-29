from abc import ABC, abstractmethod

class WeatherProvider(ABC):
    def __init__(self, api_key, website):
        self._api_key = api_key
        self._website = website

    @abstractmethod
    def get_current_weather(self, city):
        """
        Get the current weather for a given city.

        Args:
            city (str): The name of the city.

        Returns:
            dict: A dictionary containing the current weather information.
        """
        pass

    @abstractmethod
    def get_forecast(self, city):
        """
        Get the weather forecast for a given city.

        Args:
            city (str): The name of the city.

        Returns:
            list: A list of dictionaries containing forecast information.
        """
        pass

#National Weather Service https://www.weather.gov/documentation/services-web-api
class NWSWeatherProvider(WeatherProvider):
    def get_current_weather(self, city):
       pass

    @abstractmethod
    def get_forecast(self, city):
        pass