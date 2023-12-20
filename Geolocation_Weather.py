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
