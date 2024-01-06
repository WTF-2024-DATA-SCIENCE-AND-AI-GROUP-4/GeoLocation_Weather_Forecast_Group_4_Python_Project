# importing the requests module for calling APIs
import requests

def get_geolocation():
    """Get the users location using ip address and returning extracted information

    Parameters:
       None

    Return:
        lat (float): latitude of user's location
        lon (float): longitude of user's location
        city (str): city of user
        country (str): country of user
    """
    endpoint1 = 'http://ip-api.com/json/'
    try: 
        response = requests.get(endpoint1)
        response.raise_for_status()
        data = response.json()
        lat = data['lat']
        lon = data['lon']
        city = data['city']
        country = data['country']
        return lat, lon, city, country
    except requests.exceptions.HTTPError as error:
        print("Error fetching geolocation data")
        print(error.response.status_code)
        return None
# print(get_geolocation.__doc__)


def get_weather_data(lat, lon):
    """Get the users location weather forecast using ip address and returning extracted information

    Parameters:
       lat (float): latitude of user's location
       lon (float): longitude of user's location

    Return:
        date_list (list) : current date of the user
        time_list (list): 24hourly time span 
        rain_list (list): rain forecast for every hour of the day
        temperature_list (list): temperature for every hour of the day.
        snowfall_list (list) : snowfall forecast for every hour of the day.
    """
    endpoint = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m,rain,snowfall&forecast_days=1'

    try:
        response = requests.get(endpoint)
        response.raise_for_status()
        data = response.json()
        date_time_list = data['hourly']['time']
        date_list = [i[0:10] for i in date_time_list]
        time_list = [i[12:] for i in date_time_list]
        rain_list= data['hourly']['rain']
        temperature_list = data['hourly']['temperature_2m']
        snowfall_list = data['hourly']['snowfall']
        return date_list, time_list, rain_list, temperature_list, snowfall_list
               
    except requests.exceptions.HTTPError as error:
        print("Error fetching weather data")
        print(error.response.status_code)
        return None

def write_to_file(date, time_list, rain_list, temperature_list, snowfall_list):
    """writing extracted weather information to weather_data.txt file

    Parameters:
        date (str): current date of the user
        time_list (list): 24 hours time range
        rain_list (list): rain values in a 24 hours time range
        temperature_list (list): temperature values in a 24 hours time range
        snowfall_list (list): snowfall value in a 24 hours time range

    Return:
        None
       
    """
    with open('weather_data.txt','w') as text_file:
        for index, rain_value in enumerate(rain_list):
            current_time = time_list[index]
            temperature =  temperature_list[index]
            snowfall_value = snowfall_list[index]
            message = f"On {date}, at {current_time}: rain is {rain_value}mm, \
temperature is {temperature}degree celsius, snowfall is {snowfall_value}cm"
            text_file.write(message + '\n')

 
def print_weather_message(city, country, date, rain_list, temperature_list, snowfall_list):
    is_very_cold = False
    is_normal = False
    is_hot = False

    print(f"For today, {date}, in {city} {country}, the following information would be useful.")
    if 0.0 not in rain_list:
        print("There's a possibility of it raining today. Be sure to carry an umbrella.")
    if 0.0 not in snowfall_list:
        print("There's a possibility of it snowing today. Be sure to dress for the weather.")

    very_cold_temperatures = [i for i in temperature_list if i <= 0]
    hot_temperatures = [i for i in temperature_list if i > 27]
    if len(very_cold_temperatures) > 0:
        is_very_cold = True
    elif len(hot_temperatures) > 0:
        is_hot = True
    else:
        is_normal = True
     
def main():
    # Print welcome message
    print("Welcome to our Geolocation Weather program!")
    
    # Get user's location from their IP address automatically
    geolocation_data = get_geolocation()

    # Check that there are no errors arising when calling the geolocation API
    if geolocation_data is not None:
        lat, lon, city, country = geolocation_data

        # Round latitude and longitude to two decimal places for the get_weather_data() function
        lat = round(lat, 2)
        lon = round(lon, 2)

        # Get weather data at that location
        weather_data = get_weather_data(lat, lon)

        # Check that there are no errors arising when calling the weather API
        if weather_data is not None:
            date_list, time_list, rain_list, temperature_list, snowfall_list = weather_data

            # Extract date as a string
            date = date_list[0]

            # Write weather information to a file 
            write_to_file(date, time_list, rain_list, temperature_list, snowfall_list)

            # Print weather message based on data received
            print_weather_message(city, country, date, rain_list, temperature_list, snowfall_list)
        
        else:
            print("Weather data not available")
        
    else:
        print("Geolocation data not available")

# Call main function to run the code
main()