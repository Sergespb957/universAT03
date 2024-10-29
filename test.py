import pytest
import requests_mock
from main import get_random_cat_image  # Замените на имя вашего модуля


# Тест для успешного запроса
def test_get_random_cat_image_success():
    with requests_mock.Mocker() as mock:
        mock.get("https://api.thecatapi.com/v1/images/search", json=[{"url": f"https://cdn2.thecatapi.com/images/{id}.jpg"}],
                 status_code=200)

        result = get_random_cat_image()
        assert result == f"https://cdn2.thecatapi.com/images/{id}.jpg"


# Тест для неуспешного запроса
def test_get_random_cat_image_failure():
    with requests_mock.Mocker() as mock:
        mock.get("https://api.thecatapi.com/v1/images/search", status_code=404)

        result = get_random_cat_image()
        assert result is None
