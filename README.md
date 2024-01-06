# Weather Forecast Project

## Overview
This project aims to provide users with weather information based on their geolocation. It leverages various functions to obtain the user's location, fetch weather data, and present a user-friendly message about the weather conditions and write weather data to a text file.

## Contributors

### Peace:
Implemented the main() function to orchestrate the entire process, calling geolocation and weather functions, and handling errors.

### Fatimah:
Implemented the get_geolocation() function, which is responsible for obtaining the user's location based on their IP address.
Utilized the requests module to send a request to the designated API URL, extracting latitude, longitude, city, and country information from the JSON response.
Incorporated a try-except block to handle potential errors during the geolocation request.

### Chidera:
Implemented the get_weather_data(latitude, longitutude) function to fetch weather data based on the provided location.
Saved the API URL in a variable.
Attempted to fetch weather data using the provided latitude and longitude.
Called the API using the get method..
Incorporated a try-except block to handle potential errors during the geolocation request.

### Nancy:
Created the print_weather_message(weather_conditions) function to generate user-friendly messages about the weather conditions.
Provided detailed logic for generating messages based on weather conditions.
Printed a message string.

### Folayemi:
Wrote information about the weather data to a text file.

### Titilayo:
Collaborated with Nancy on the print weather message function to update function logic.

### Uduak:
Collaborated on error handling within the get_weather_data function.
Handled HTTP errors during the weather data request.

### Ibinabo:
Responsible for all forms of documentation.
Set up the GitHub repository.
Resolved conflicts and merged pull requests to the main branch.
Ensured team collaboration.
Set up and organized team meetings.
Created presentation documents.

### Gladys:
Collaborated on error handling within the geolocation function.
Handled HTTP errors during the weather data request.

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
To run the program, execute the main() function. Observe the generated weather information and messages.

## Important Note
Ensure that you have internet connectivity for smooth running.

