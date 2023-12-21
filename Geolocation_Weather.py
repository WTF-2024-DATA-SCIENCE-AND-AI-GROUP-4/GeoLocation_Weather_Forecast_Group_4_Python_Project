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


def get_weather_data():
    """Get the users location weather forecast using ip address and returning extracted information

    Parameters:
       temperature in celsius
       rain in milimeters
       snowfall in centimeters
       date and time

    Return:
        lat (float): latitude of user's location
        lon (float): longitude of user's location
        city (str): city of user
        country_code (str): country_code of user
    """
    endpoint = 'https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m,rain,snowfall&forecast_days=1'

    try:
        payload = {
            'q': 'Abuja,Nigeria',
            'unit':'metrics',
            }
        response = requests.get(url=endpoint, params=payload)
        print(response.status_code)
        data = response.json()
        date_time_list = data['hourly']['time']
        date_list = [i[0:10] for i in date_time_list]
        time_list = [i[12:] for i in date_time_list]
        rain_list= data['hourly']['rain']
        temperature_list = data['hourly']['temperature_2m']
        snowfall_list = data['hourly']['snowfall']
        print(date_time_list)
        print()
        print(rain_list)
        print()
        print(temperature_list)
        print()
        print(snowfall_list)
    except:
        pass
print(get_weather_data())