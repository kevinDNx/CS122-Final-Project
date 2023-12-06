#Code Tkinter Frontend Here
from urllib import response
from weather_backend import *


# Update the weekly weather forecast
weekly_weather = update()

# image cache list
img_cache = []

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

print(weekly_weather[0].get_temperature())
print(weekly_weather[1].get_temperature())
print(weekly_weather[2].get_temperature())

print(weekly_weather[1].get_short_forecast())
print(weekly_weather[1].get_detailed_forecast())
print(weekly_weather[1].get_icon_url())
print(weekly_weather[1].get_start_time())
print(weekly_weather[1].get_end_time())

import tkinter as tk
import requests
from PIL import Image, ImageTk
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


class WeatherApp(tk.Frame):
    def __init__(self, master):
        self.switch = False
        self.detailed = False
        super().__init__(master)

        # Create top section
        top_section = tk.Frame(self)
        top_section.pack(side="top", fill="both")

        # Add title label with neutral and factually accurate text
        title_label = tk.Label(top_section, text="Weekly Forecast Overview", font=("Arial", 20))
        title_label.pack(pady=10)

        for i in range(0,len(weekly_weather)):
            output_file = f'imgcache/{i}.png'
            icon_url = weekly_weather[i].get_icon_url()
            response = requests.get(icon_url)
            with open(output_file, 'wb') as f:
                for chunk in response:
                    f.write(chunk)

            img_cache.append

        # Create empty slots with outlines and day names
        self.weather_slots = []
        y = 0
        for i, day in enumerate(weekly_weather):
            if i % 2 == self.switch:
                slot_frame = self.create_weather_slot(top_section, i, day)
                self.weather_slots.append(slot_frame)
                
            y += 1
        
        # Create bottom section
        bottom_section = tk.Frame(self)
        bottom_section.pack(side="bottom", fill="both")

        self.am_pm_button = tk.Button(bottom_section, text="AM/PM", command=lambda: self.toggle_display_mode(top_section))
        self.am_pm_button.pack(fill="x", expand=True)

        details_button = tk.Button(bottom_section, text="Detailed", command=lambda: self.toggle_detailed_mode(top_section))
        details_button.pack(fill="x", expand=True)

        trends_button = tk.Button(bottom_section, text="Trends", command=lambda: self.open_trends_window())
        trends_button.pack(fill="x", expand=True)




    def toggle_display_mode(self, topsection):
        self.switch = not self.switch

        # Remove existing weather slots
        for slot_frame in self.weather_slots:
            slot_frame.destroy()

        self.weather_slots = []

        # Create new weather slots based on the current mode
        y = 0
        for i, day in enumerate(weekly_weather):
            if i % 2 == self.switch:
                slot_frame = self.create_weather_slot(topsection, i, day)
                self.weather_slots.append(slot_frame)
                y += 1

    def toggle_detailed_mode(self, topsection):
        self.detailed = not self.detailed
        # Remove existing weather slots
        for slot_frame in self.weather_slots:
            slot_frame.destroy()

        self.weather_slots = []

        # Create new weather slots based on the current mode
        y = 0
        for i, day in enumerate(weekly_weather):
            if i % 2 == self.switch:
                slot_frame = self.create_weather_slot(topsection, i, day)
                self.weather_slots.append(slot_frame)
                y += 1


    def create_weather_slot(self, topsection, i, day):
        slot_frame = tk.Frame(topsection, borderwidth=2, relief="groove", highlightthickness=1)
        # Anchor the frame to the top
        slot_frame.pack(side="left", anchor="n", padx=10)

        # Add day name label
        day_label = tk.Label(slot_frame, text=f"{day.get_name()}", font=("Arial", 12))
        day_label.pack(pady=5)

        # Load and display the cached icon
        icon_file = f"imgcache/{i}.png"
        img = Image.open(icon_file)
        img = img.resize((50, 50))  # Adjust image size as needed
        img_tk = ImageTk.PhotoImage(img)
        icon_label = tk.Label(slot_frame, image=img_tk)
        icon_label.image = img_tk  # To prevent garbage collection
        icon_label.pack()

        # Add forecast text
        if self.detailed:
            forecast = day.get_detailed_forecast()
            forecast_label = tk.Label(slot_frame, text=forecast, font=("Arial", 8), wraplength=100)  # Wrap text after 100 pixels
            forecast_label.pack(pady=5)

        else:
            # Get and display the temperature
            temperature = day.get_temperature()
            temperature_label = tk.Label(slot_frame, text=f"{temperature}°F", font=("Arial", 10))
            temperature_label.pack(pady=5)

            forecast = day.get_short_forecast()
            forecast_label = tk.Label(slot_frame, text=forecast, font=("Arial", 8), wraplength=100)  # Wrap text after 100 pixels
            forecast_label.pack(pady=5)

        return slot_frame
    
    def open_trends_window(self):
        # Create a new window
        trends_window = tk.Toplevel(self)
        trends_window.title("Trends")

        # Create the main frame
        main_frame = tk.Frame(trends_window)
        main_frame.pack(fill="both", expand=True)
        # Add a label for the window title
        trends_label = tk.Label(trends_window, text="Weather Trends: Temperature", font=("Arial", 16))
        trends_label.pack(pady=10)
        # Split the frame left and right
        left_frame = tk.Frame(main_frame)
        left_frame.pack(side="left", fill="both", expand=True)

        right_frame = tk.Frame(main_frame)
        right_frame.pack(side="right", fill="both", expand=True)

        # Define two subframes within the right_frame
        right_column1 = tk.Frame(right_frame)
        right_column1.pack(side="left", fill="both", expand=True)

        temperature_button = tk.Button(right_column1, text="Temperature")
        temperature_button.pack(pady=2)

        precipitation_button = tk.Button(right_column1, text="Precipitation")
        precipitation_button.pack(pady=2)

        wind_speed_button = tk.Button(right_column1, text="Wind Speed")
        wind_speed_button.pack(pady=2)


        right_column2 = tk.Frame(right_frame)
        right_column2.pack(side="left", fill="both", expand=True)

        wind_direction_button = tk.Button(right_column2, text="Wind Direction")
        wind_direction_button.pack(pady=2)

        dew_point_button = tk.Button(right_column2, text="Dew Point")
        dew_point_button.pack(pady=2)

        relative_humidity_button = tk.Button(right_column2, text="Relative Humidity")
        relative_humidity_button.pack(pady=2)

        temperature_button.pack(pady=5, fill="x")
        precipitation_button.pack(pady=5, fill="x")
        wind_speed_button.pack(pady=5, fill="x")

        wind_direction_button.pack(pady=5, fill="x")
        dew_point_button.pack(pady=5, fill="x")
        relative_humidity_button.pack(pady=5, fill="x")

        # Import NumPy for polynomial fit

        

        # Create a placeholder figure for the graph
        fig, ax = plt.subplots(figsize=(5, 3))

        # Generate mock temperature data for 14 days
        mock_data = [66, 62, 60, 66, 65, 62, 63]

        # Extract x and y data points
        x = range(7)
        y = mock_data

        # Calculate the coefficients of the trend line
        z = np.polyfit(x, y, 1)
        trend_line = np.poly1d(z)

        # Plot the data as a line graph
        ax.plot(range(7), mock_data)
        ax.plot(x, trend_line(x), color="red", linestyle="--", linewidth=1)

        # Set axis labels
        ax.set_xlabel("Day")
        ax.set_ylabel("Temperature (°F)")

        # Add title
        ax.set_title("Temperature Trend (12/6 - 12/13)")

        # Convert the figure to an image for Tkinter
        canvas = FigureCanvasTkAgg(fig, master=left_frame)
        canvas.get_tk_widget().pack(fill="both", expand=True)

        





if __name__ == "__main__":
    root = tk.Tk()
    root.title("WeatherMate")
    root.minsize(width=900, height=500)
    root.maxsize(width=1000, height=900)

    app = WeatherApp(root)
    app.pack(fill="both", expand=True)

    root.mainloop()










