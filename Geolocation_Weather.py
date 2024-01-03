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
        country_code (str): country_code of user
    """
    endpoint1 = 'http://ip-api.com/json/'
    try: 
        response = requests.get(endpoint1)
        data = response.json()
        # print(data)
        lat = data['lat']
        lon = data['lon']
        city = data['city']
        country_code = data['countryCode']
        return lat, lon, city, country_code
    except:
        pass
print(get_geolocation())
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