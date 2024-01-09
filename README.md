# Weather Forecast Project

## Overview
This project aims to provide users with weather information based on their geolocation. It leverages various functions to obtain the user's location, fetch weather data, and present a user-friendly message about the weather conditions and write weather data to a text file.

## Contributors

### [Peace Adamson](https://github.com/thatpeacegirl)
+ Implemented the main() function to orchestrate the entire process.
+ Calling geolocation and weather functions.
+ Handling errors.

### [Fatimah Animashaun](https://github.com/FatimahAnimashaun):
+ Implemented the get_geolocation() function, which is responsible for obtaining the user's location based on their IP address.
+ Utilized the requests module to send a request to the designated API URL, extracting latitude, longitude, city, and country information from the JSON response.
+ Incorporated a try-except block to handle potential errors during the geolocation request.

### [Chidera Mba](https://github.com/ChideraFrancisca):
+ Implemented the get_weather_data(latitude, longitutude) function to fetch weather data based on the provided location.
+ Saved the API URL in a variable.
+ Attempted to fetch weather data using the provided latitude and longitude.
+ Called the API using the get method..
+ Incorporated a try-except block to handle potential errors during the geolocation request.

### [Nancy Dzikunu-Bansah](https://github.com/AnatabaKyorku):
+ Created the print_weather_message(weather_conditions) function to generate user-friendly messages about the weather conditions.
+ Provided detailed logic for generating messages based on weather conditions.
+ Printed a message string.

### [Folayemi Oladotun](https://github.com/TechyFola):
+ Wrote information about the weather data to a text file.
+ Ensured team collaboration.
+ Set up and organized team meetings.

### [Titilayo Dada](https://github.com/TITILAYODADA):
+ Collaborated with Nancy on the print weather message function to update function logic.

### [Uduak Njoku](https://github.com/UduakN):
+ Collaborated on error handling within the get_weather_data function.
+ Handled HTTP errors during the weather data request.

### [Ibinabo Adiela](https://github.com/lilyflowr):
+ Responsible for all forms of documentation.
+ Set up the GitHub repository.
+ Resolved conflicts and merged pull requests to the main branch.
+ Ensured team collaboration.
+ Set up and organized team meetings.
+ Created presentation documents.

### [Gladys Emmanuel](https://github.com/Oziohuu):
+ Collaborated on error handling within the geolocation function.
+ Handled HTTP errors during the weather data request.


# APIs Used
We utitlized two APIs for our project.
+ Weather API sourced from [Open-Meteo.com](http://Open-Meteo.com)
API link:https://api.open-meteo.com

+ Geolocation API sourced from [ipwhois.io](http://ipwhois.io)
API link:http://ip-api.com/


# Functionality

## get_geolocation()
Obtains the user's location using their IP address.
Returns latitude, longitude, city, and country information.

## get_weather_data(lat, lon)
Fetches weather data based on the provided latitude and longitutde.
Returns date, time, rain forecast, temperature, and snowfall information for a 24-hour span.

## write_to_file(weather conditions):
Writes extracted weather information to a file named weather_data.txt.

## print_weather_message(weather_conditions)
Generates user-friendly weather messages based on temperature and weather conditions.
Provides suggestions for the day, considering rainy, sunny, or other weather conditions.

## main()
Orchestrates the entire process, calling geolocation and weather functions, and handling errors.
Generates an introductory message.


## Usage
### Pre-requisites
1. Install Python:
+ If you don't have Python installed, follow this guide on [How to install Python](https://realpython.com/installing-python/).

2. Install git
+ If you do not have git installed, follow this guide on [How to install git on Window, Mac Os and Linux](https://kinsta.com/knowledgebase/install-git/)

3. Install your favourite IDE.
+ In this guide we would use VsCode

4.  Install required dependencies
+ Open your terminal or command prompt and run the following command to install the necessary module:

```bash
pip install requests
```
+ If this method doesn't work use the following command:

```

```
3. Clone the repository:
+ Copy the repository's URL:
 https://github.com/WTF-2024-DATA-SCIENCE-AND-AI-GROUP-4/GeoLocation_Weather_Forecast_Group_4_Python_Project.git

+ In your terminal, navigate to the directory where you want to clone the project and run:

```bash
git clone https://github.com/WTF-2024-DATA-SCIENCE-AND-AI-GROUP-4GeoLocation_Weather_Forecast_Group_4_Python_Project.git
```


4. Navigate to the project directory:
+ Change your working directory to the cloned project folder:

```bash
cd GeoLocation_Weather_Forecast_Group_4_Python_Project\
```

5. Run the program:
+ Run the code by clicking the run icon ![run icon](https://i.imgur.com/ZQJEyvd.png) or use the shortcut (Ctrl/Cmd+Alt+N)
+ Observe the generated weather information and messages.
+ The program will display weather information and messages based on your geolocation.
+ This is an example of the information you will get when you run the code:
![weatherTextFile](https://i.imgur.com/ST7cxa5.png)

Now you can successfully use the Weather Forecast Project on your local machine. 

## Important Note
+ Make sure to have internet connectivity for smooth running.

## Limitations:
+ The Geolocation API gives an approximate location.
+ This limitation is due to the guidelines for this project (Making use of Keyless APIs)

## Further Improvements Going Forward:
+ Creating a user-friendly website that can automatically detect the user's location and gives customized weather forecasts.
