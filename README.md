# CS122-Final-Project

# Project Title: WeatherMate (Working title)

Authors: Kevin Nguyen, Daniel Bao

Project Description (5 Sentences)

The WeatherMate App is a project that will provide users with a sleek and user-friendly interface, making it easy to access a wealth of weather information at a glance. It offers real-time weather updates, including temperature, humidity, wind speed, and precipitation forecasts for their current location. The app will gather data from multiple sites and organize the data. Users can also explore weather data for any location globally, enabling travel planning with ease. With interactive maps, detailed weather charts and graphs, this app will keep users informed and prepared for any weather event. It will provide details on the weather for up to 5 days. 

Project Outline/Plan
1. Data Collection and Storage:

For data collection, we will utilize Python libraries and packages such as requests and BeautifulSoup to fetch data from various sources, including the official website of the [National Weather Service](https://www.weather.gov/documentation/services-web-api), [OpenWeatherMap](https://openweathermap.org/api), and [AccuWeather API](https://developer.accuweather.com/user/register). To ensure efficient and responsible data retrieval, the collected information will be stored in a text file, a prudent choice that helps prevent over-calling of the APIs and ensures the availability of the data for future analysis and usage. This approach allows us to maintain data integrity and minimize unnecessary network requests while enabling easy data access and management.

3. Analysis and Visualization.

To enhance data visualization, we will integrate Matplotlib and Plotly, enabling dynamic and interactive graphs and charts. Users can explore their data in an engaging and insightful manner, with options to zoom, pan, and analyze data points. Furthermore, Folium will be used to seamlessly incorporate interactive maps, enabling users to visualize geospatial data with ease. This combination of Tkinter, Matplotlib, Plotly, and Folium ensures that our interface not only conveys information effectively but also offers an engaging and visually appealing user experience.

5. Interface.

Our interface plan will employ the Tkinter library as the foundation for a user-friendly and intuitive graphical interface. Tkinter will provide a familiar and responsive platform for users to interact with our application. There will be a tab to switch between the visualization of different data visualizations. 

Data Collection and Storage Plan (written by Author #1)

Data Analysis and Visualization Plan (Author #2)

A .gitignore file and a license
