import pytest
import requests
from main_thecat import get_cat_image


def test_get_cat_image(mocker):
    mock_get = mocker.patch('main_thecat.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [{
        "id": "DEbrbE0_7",
        "url": "https://cdn2.thecatapi.com/images/DEbrbE0_7.jpg",
        "width": 1600,
        "height": 1009
    }]

    image = get_cat_image()

    image_url = "https://cdn2.thecatapi.com/images/DEbrbE0_7.jpg"

    assert image == requests.get(image_url).content


def test_get_cat_image_error(mocker):
    mock_get = mocker.patch('main_thecat.requests.get')
    mock_get.return_value.status_code = 404

    image_data = get_cat_image()

    assert image_data is None
