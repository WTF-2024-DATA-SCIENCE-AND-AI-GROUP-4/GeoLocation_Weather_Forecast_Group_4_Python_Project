# importing the requests module for calling APIs
#import requests
from pip._vendor import requests
from datetime import datetime as dt
from pprint import pprint as pp

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
        data = response.json()
        lat = data['lat']
        lon = data['lon']
        city = data['city']
        country = data['country']
        return lat, lon, city, country
    except:
        pass
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
        print(response.status_code)
        data = response.json()
        date_time_list = data['hourly']['time']
        date_list = [i[0:10] for i in date_time_list]
        time_list = [i[12:] for i in date_time_list]
        rain_list= data['hourly']['rain']
        temperature_list = data['hourly']['temperature_2m']
        snowfall_list = data['hourly']['snowfall']
        return date_list, time_list, rain_list, temperature_list, snowfall_list
               
    except:
        pass
print(get_weather_data())

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
    is_snowy = False
    print(f"For today, {date}, in {city} {country}, the following information would be useful.")
    for rain_value in rain_list:
        if rain_value > 0.0:
            is_rainy = True
    for temperature in temperature_list:
        if temperature <= 0:
            print("It's going to be chilly today. Be sure to dress warm!")
            break
        elif temperature < 27:
            print("It's going to be quite cold today. Be sure to carry a sweater!")
            break
        else:
            is_rainy = False
    for snow_value in snowfall_list:
        if snow_value < 0.0:
            is_snowy = True  
    
    
