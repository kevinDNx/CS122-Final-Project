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
# if day_one.temperature_day is not None:
#     print(f"Day One (Daytime): {day_one.temperature_day.get_name()}")
# else:
#     print("Day One (Nighttime): Skipped due to nighttime forecast")


#-----------------------------------------------#


# accesing more of the raw data by calling this total of 14 days and nights combined
weekly_weather = get_weekly_average()

# print(weekly_weather[0].get_name())
# print(weekly_weather[1].get_name())
# print(weekly_weather[2].get_name())
# print(weekly_weather[3].get_name())
# print(weekly_weather[4].get_name())

# print(weekly_weather[0].get_temperature())
# print(weekly_weather[1].get_temperature())
# print(weekly_weather[2].get_temperature())

# print(weekly_weather[1].get_short_forecast())
# print(weekly_weather[1].get_detailed_forecast())
# print(weekly_weather[1].get_icon_url())
# print(weekly_weather[1].get_start_time())
# print(weekly_weather[1].get_end_time())

import tkinter as tk
import requests
from PIL import Image, ImageTk
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import re


class WeatherApp(tk.Frame):
    def __init__(self, master):
        self.switch = False
        self.detailed = False
        super().__init__(master)

        top_section = tk.Frame(self)
        top_section.pack(side="top", fill="both")

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
        slot_frame.pack(side="left", anchor="n", padx=10)

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
        """
        Opens a new window containing buttons for different weather trends.
        """
        # Create a new toplevel window
        trends_window = tk.Toplevel(self)
        trends_window.title("Trends")
        trends_window.minsize(width=450, height=250)
        trends_window.maxsize(width=500, height=450)

        # Add label for window title
        trends_label = tk.Label(trends_window, text="Weather Trends:", font=("Arial", 16))
        trends_label.pack(pady=10)

        # Define a frame to hold the buttons
        button_frame = tk.Frame(trends_window)
        button_frame.pack(fill="both", expand=True)

        # Create buttons for each trend
        trend_buttons = {
            "Temperature": tk.Button(button_frame, text="Temperature", command= lambda: self.create_graph("Temperature")),
            "Precipitation": tk.Button(button_frame, text="Precipitation", command= lambda: self.create_graph("Precipitation")),
            "Wind Speed": tk.Button(button_frame, text="Wind Speed", command= lambda: self.create_graph("Wind Speed")),
            "Dew Point": tk.Button(button_frame, text="Dew Point", command= lambda: self.create_graph("Dew Point")),
            "Relative Humidity": tk.Button(button_frame, text="Relative Humidity", command= lambda: self.create_graph("Relative Humidity")),
        }

        # Pack the buttons in a grid layout
        for i, (trend, button) in enumerate(trend_buttons.items()):
            button.pack(fill="x")

    def create_graph(self, trend):

        graph_window = tk.Toplevel(self)
        graph_window.title(f"{trend} Trend")
        graph_window.minsize(width=900, height=500)
        graph_window.maxsize(width=1000, height=900)

        fig, ax = plt.subplots(figsize=(5, 3))
        plt.subplots_adjust(left=0.15, right=0.95, bottom=0.15, top=0.95)

        names, y = self.get_graph_info(trend)
        x = range(14)

        z = np.polyfit(x, y, 1)
        trend_line = np.poly1d(z)

        high_index = np.argmax(y)
        low_index = np.argmin(y)

        high_value = y[high_index]
        low_value = y[low_index]

        ax.annotate(f"High: {high_value}", xy=(x[high_index], high_value), color="green")
        ax.annotate(f"Low: {low_value}", xy=(x[low_index], low_value), color="blue")

        ax.plot(range(14), y, color="skyblue", linewidth=2)
        ax.plot(x, trend_line(x), color="orange", linestyle=":", linewidth=1)

        ax.set_xlabel("Forecast Interval", fontweight="bold", fontsize=12)
        if (trend == "Temperature"):
            ax.set_ylabel("Temperature (°F)", fontweight="bold", fontsize=12)
        if (trend == "Precipitation"):
            ax.set_ylabel("Precipitation Chance (%)", fontweight="bold", fontsize=12)
        if (trend == "Wind Speed"):
            ax.set_ylabel("Wind Speed (mph)", fontweight="bold", fontsize=12)
        if (trend == "Dew Point"):
            ax.set_ylabel("Dew Point (°C)", fontweight="bold", fontsize=12)
        if (trend == "Relative Humidity"):
            ax.set_ylabel("Relative Humidity (%)", fontweight="bold", fontsize=12)        
        ax.set_title(f"{trend} Trend ({names[0]} - {names[-1]})", fontweight="bold", fontsize=14)


        ax.set_xticks(range(len(names)))
        ax.set_xticklabels(names, rotation=45, ha="right", fontsize=8)


        ax.grid(True, which="both", linestyle="--", linewidth=0.5, color="gray")

        # Convert the figure to a Tkinter canvas
        canvas = FigureCanvasTkAgg(fig, master=graph_window)
        canvas.get_tk_widget().pack(fill="both", expand=True)

        # Display the graph window
        graph_window.mainloop()

    def get_graph_info(self, trend):
        names = []
        y = []
        for i in range(0,len(weekly_weather)):
            names.append(weekly_weather[i].get_name())

            if (trend == "Temperature"):
                y.append(weekly_weather[i].get_temperature())
            elif (trend == "Precipitation"):
                y.append(weekly_weather[i].get_probability_of_precipitation())
                if y[i] == None:
                    y[i] = 0
            elif (trend == "Wind Speed"):
                y.append(weekly_weather[i].get_wind_speed())
                # Extract all numbers using regular expressions
                numbers = re.findall(r"\d+", y[i])
                # Convert strings to integers
                numbers = [int(num) for num in numbers]
                # Find and print the highest number
                y[i] = max(numbers)
            elif (trend == "Dew Point"):
                y.append(weekly_weather[i].get_dewpoint())
            elif (trend == "Relative Humidity"):
                y.append(weekly_weather[i].get_relative_humidity())
        
        # print(names)
        # print(y)
        return names, y

 

        





if __name__ == "__main__":
    root = tk.Tk()
    root.title("WeatherMate")
    root.minsize(width=900, height=500)
    root.maxsize(width=1000, height=900)

    app = WeatherApp(root)
    app.pack(fill="both", expand=True)

    root.mainloop()










