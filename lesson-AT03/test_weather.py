import pytest
from main_weather import get_weather

from config import API_WEATHER_KEY


def test_get_weather(mocker):
    mock_get = mocker.patch('main_weather.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'weather': [{'description': 'sunny'}],
        'main': {'temp': 15.5}
    }

    api_key = API_WEATHER_KEY
    city = 'London'

    weather_data = get_weather(api_key, city)

    assert weather_data == {
            'weather': [{'description': 'sunny'}],
            'main': {'temp': 15.5}
        }


def test_get_weather_error(mocker):
    mock_get = mocker.patch('main_weather.requests.get')
    mock_get.return_value.status_code = 404

    api_key = API_WEATHER_KEY
    city = 'London'

    weather_data = get_weather(api_key, city)

    assert weather_data is None
