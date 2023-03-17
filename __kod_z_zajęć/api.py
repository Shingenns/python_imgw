import requests
import json
from requests.exceptions import HTTPError


def get_data_by_datapoint(datapoint: str, api_key: str):

    base_url = 'http://api.openweathermap.org/geo/1.0/direct'
    try:
        response = requests.get(base_url,
            params={'q': datapoint,
                    'appid': api_key,
                    'limit': 5,
                    'lang': 'pl'},
            timeout=3.0
        )

        # wyjątek nie zostanie zgłoszony jeżeli status == OK
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'Błąd HTTP: {http_err}')
    except Exception as err:
        print(f'Inny wyjątek: {err}')
    else:
        print('OK!')
        return response.json()


def get_lon_and_lat(json_data) -> dict:
    """returns lat and lon for datapoint"""
    point_data = {
        'name': json_data[0]['name'],
        'lat': json_data[0]['lat'],
        'lon': json_data[0]['lon']
        }
    return point_data


def get_weather_data(coords):
    base_url = 'https://api.openweathermap.org/data/2.5/weather'

    try:
        response = requests.get(base_url,
            params={'lat': coords['lat'],
                    'lon': coords['lon'],
                    #'exclude': 'hourly,daily',
                    'appid': api_key,
                    'lang': 'pl'},
            timeout=3.0
        )

        # wyjątek nie zostanie zgłoszony jeżeli status == OK
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'Błąd HTTP: {http_err}')
    except Exception as err:
        print(f'Inny wyjątek: {err}')
    else:
        print('OK!')
        return response.json()



if __name__ == '__main__':
    api_key = '715008316b246c53036d6cd738a42d2d'
    base_url = 'http://api.openweathermap.org/geo/1.0/direct'
    city = 'Olsztyn'


    # zapisujemy json, aby nie odpytywać API o dane dla miasta
    # za każdym razem - zapisujemy tylko raz, więc poniższy fragment po zapisaniu można zakomentować
    # data = get_data_by_datapoint(city, api_key)
    # with open('datapoints.json', 'w') as plik:
    #     json.dump(data, plik)


    with open('datapoints.json', 'r') as plik:
        loaded_data = json.load(plik)
    
    print(loaded_data)
    coords = get_lon_and_lat(loaded_data)
    print(get_weather_data(coords))
