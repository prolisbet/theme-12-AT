import pytest
from main_github import get_github_user


def test_get_github_user(mocker):
    mock_get = mocker.patch('main_github.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'login': 'lisbet96',
        'id': 730408,
        'name': 'Liza'
    }

    user_data = get_github_user('cat')

    assert user_data == {
        'login': 'lisbet96',
        'id': 730408,
        'name': 'Liza'
    }


def test_get_github_user_error(mocker):
    mock_get = mocker.patch('main_github.requests.get')
    mock_get.return_value.status_code = 500

    user_data = get_github_user('lisbet96')

    assert user_data is None
