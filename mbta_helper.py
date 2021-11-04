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

print(get_lat_long('Boston,MA'))


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    APIKEY = 'db0316857dfa4ca7883570a48992b29d'
    location  = place_name
    url = f'https://www.mbta.com/data/{inlatitudedex}/attributes/latitude, /data/{index}/attributes/longitude'
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    Location = (response_data['results'][0]['locations'][0]['displayLatLng']['lat'],response_data['results'][0]['locations'][0]['displayLatLng']['lng'])
    return Location
    


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """
    pass


def main():
    """
    You can test all the functions here
    """
    pass


if __name__ == '__main__':
    main()
