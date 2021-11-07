# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"     

# Your API KEYS (you need to use your own keys - very long random characters)
MAPQUEST_API_KEY = ""
MBTA_API_KEY = ""


# A little bit of scaffolding if you want to use it

import urllib.request
import json


def get_json(url):
    operUrl = urllib.request.urlopen(url)
    data = operUrl.read()
    return data


def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding  API URL formatting requirements.
    """

    APIKEY = 'jQgutkIaKpzETRioBxfWDLFBloBfG5aI'
    location  = place_name
    url = f'http://www.mapquestapi.com/geocoding/v1/address?key={APIKEY}&location={location}'
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    Location = (response_data['results'][0]['locations'][0]['displayLatLng']['lat'],response_data['results'][0]['locations'][0]['displayLatLng']['lng'])
    return Location

# print(get_lat_long('Boston,MA'))


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    APIKEY = 'db0316857dfa4ca7883570a48992b29d'
    url = f'https://api-v3.mbta.com/stops?api_key={APIKEY}&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}'
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    wheel = ''
    n = 0
    while wheel is not 'Wheel Chair Accessible':
        wheel1 = int(response_data['data'][n]['attributes']['wheelchair_boarding'])
        if wheel1 == 1:
            wheel = 'Wheel Chair Accessible'
        elif wheel1 == 2:
            wheel = 'Wheel Chair Inaccessible'
        else: wheel = 'Accessibility: No Information'
        n+1
    info = (response_data['data'][0]['attributes']['name'],wheel)
    return info
    
    
    
# print(get_nearest_station(42.358894,-71.056742))

def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """
    lat_long = get_lat_long(place_name)
    lat = lat_long[0]
    longtitude = lat_long[1]
    return get_nearest_station(lat,longtitude)
    

def main():
    """
    You can test all the functions here
    """
    print(find_stop_near(Newton, MA)


if __name__ == '__main__':
    main()
