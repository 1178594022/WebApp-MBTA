import urllib.request
import json


def get_lat_long(place_name):
    """
    Take a place name or address as a arguement, and return a (latitude, longitude) tuple
    with the coordinates of the given place.
    """
    """
    request the data using the api key, with location equals to the input. define the veriable response_text to 
    store the text file, and response_data to store it in the format of jason. Then return a tupple of (latitude,longtitude)
    """
    APIKEY = 'jQgutkIaKpzETRioBxfWDLFBloBfG5aI'
    location = place_name.replace(" ","")
    url = f'http://www.mapquestapi.com/geocoding/v1/address?key={APIKEY}&location={location}'
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    Location = (response_data['results'][0]['locations'][0]['displayLatLng']['lat'],
                response_data['results'][0]['locations'][0]['displayLatLng']['lng']) 
    return Location

# print(get_lat_long('Boston,MA'))


def get_nearest_station(latitude, longitude):
    """
    Takes two arguement which are latitude and longitude strings to return a tupple of (station_name, wheelchair_accessible)
    for the nearest MBTA station to the given coordinates.
    """
    APIKEY = 'db0316857dfa4ca7883570a48992b29d'
    url = f'https://api-v3.mbta.com/stops?api_key={APIKEY}&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}'
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    '''
    all  of the green commented portion can be used to find the nearest wheel chair accessable stop of MBTA station. 
    If use comment line 65 to 71
    '''
    # wheel = ''
    # n = 0
    # while wheel != 'Wheel Chair Accessible':
    #     wheel1 = int(response_data['data'][n]['attributes']['wheelchair_boarding'])
    #     if wheel1 == 1:
    #         wheel = 'Wheel Chair Accessible'
    #     elif wheel1 == 2:
    #         wheel = 'Wheel Chair Inaccessible'
    #     else: wheel = 'Accessibility: No Information'
    #     n+1
    wheel1 = 0 # set veriable
    wheel1 = int(response_data['data'][0]['attributes']['wheelchair_boarding']) # set wheel1 equals to where the closest stations accessability is stored
    """changing the un-story telling number indicator to its meaning behind"""
    if wheel1 == 1:
        wheel = 'Wheel Chair Accessible'
    elif wheel1 == 2:
        wheel = 'Wheel Chair Inaccessible'
    else:
        wheel = 'No Information'
    """create and return the tupple(station_name, wheelchair_accessible)"""
    info = (response_data['data'][0]['attributes']['name'], wheel)
    return info


# print(get_nearest_station(42.358894,-71.056742))

def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """
    lat_long = get_lat_long(place_name) # get the (lat,long)tupple
    lat = lat_long[0] # set veriable to store latitude
    longtitude = lat_long[1] # set veriable to store longtitude
    try: # if the address can find a station, return the following
        return get_nearest_station(lat, longtitude) # find the neatest station and returns it.
    except: # when error return none
        return None
# print(find_stop_near('Newton,MA'))


def main():
    print(find_stop_near('Newton,MA'))


if __name__ == '__main__':
    main()
