import tkinter as tk
from tkinter import ttk
from weather_backend import WeatherDay, run_check, get_current_location, get_weekly_average_forecast
import datetime

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")

        self.label = ttk.Label(self.root, text="Weekly Weather Forecast")
        self.label.pack(pady=10)

        self.text_output = tk.Text(self.root, height=15, width=90)
        self.text_output.pack()

        self.refresh_button = ttk.Button(self.root, text="Refresh", command=self.refresh_weather)
        self.refresh_button.pack(pady=10)

    def refresh_weather(self):
        if run_check():
            latitude, longitude = get_current_location()
            weekly_average = get_weekly_average_forecast(latitude, longitude)

            weekly_average_weather = self.create_weekly_average_weather(weekly_average)

            # Display the weather information
            self.display_weather(weekly_average_weather)
        else:
            self.text_output.delete(1.0, tk.END)
            self.text_output.insert(tk.END, "Checks failed. Unable to fetch weather data.")

    def create_weekly_average_weather(self, weekly_average):
        weekly_average_weather = []
        current_date = datetime.date.today()

        for i in range(0, len(weekly_average), 2):
            day1_day_temperatures = weekly_average[i]
            day1_night_temperatures = weekly_average[i + 1]
            weekly_average_weather.append(WeatherDay(current_date, day1_day_temperatures, day1_night_temperatures))
            current_date += datetime.timedelta(days=1)

        return weekly_average_weather

    def display_weather(self, weekly_average_weather):
        self.text_output.delete(1.0, tk.END)

        for day in weekly_average_weather:
            weather_info = str(day) + "\n\n"
            self.text_output.insert(tk.END, weather_info)

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
