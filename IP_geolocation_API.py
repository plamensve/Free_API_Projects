import requests


def geo_location_api():
    url = 'http://ipwho.is/52.33.28.100'

    try:
        response = requests.get(url)
        date = response.json()
        rate_ip = date['ip']
        rate_continent = date['continent']
        rate_country = date['country']
        rate_region = date['region']
        rate_city = date['city']
        rate_postal_code = date['postal']
        rate_latitude = date['latitude']
        rate_longitude = date['longitude']
        return rate_ip, rate_continent, rate_country, rate_region, rate_city, rate_postal_code, rate_latitude, rate_longitude

    except requests.exceptions.RequestException as e:
        print('Error')


print(geo_location_api())
#test