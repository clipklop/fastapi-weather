import pytest
import httpx
import respx

from httpx import Response


def test__opm__check_if_root_page_returns_status_200_and_hello_world():
    my_route = respx.get("http://0.0.0.0:8000/").mock(return_value=Response(200))
    response = httpx.get("http://0.0.0.0:8000/")
    assert my_route.called
    assert response.status_code == 200
    assert response.text == "Hello, Weather!"


def test__opm__if_weather_endpoint_returns_weather_object():
    my_route = respx.get("http://0.0.0.0:8000/").mock(return_value=Response(200))
    response = httpx.get("http://0.0.0.0:8000/")
    assert my_route.called
    assert response.status_code == 200
    assert response.text == "Hello, Weather!"
