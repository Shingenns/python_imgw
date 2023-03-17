import requests
from requests.exceptions import HTTPError


def get_data_by_datapoint(datapoint: str, api_key: str):

    base_url = 'http://api.openweathermap.org/geo/1.0/direct'
    try:
        response = requests.get(base_url,
            params={'q': datapoint, 'appid': api_key, 'limit': 5},
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


def get_lon_and_lat(json_data):
    """returns lat and lon for datapoint"""
    pass


if __name__ == '__main__':
    api_key = '715008316b246c53036d6cd738a42d2d'
    base_url = 'http://api.openweathermap.org/geo/1.0/direct'
    city = 'Olsztyn'

    print(get_data_by_datapoint(city, api_key))
