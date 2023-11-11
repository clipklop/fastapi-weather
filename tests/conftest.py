import httpx
import respx
import pytest

from httpx import Response


@respx.mock
def test_example():
    my_route = respx.get("http://0.0.0.0:8000/").mock(return_value=Response(204))
    response = httpx.get("http://0.0.0.0:8000/")
    assert my_route.called
    assert response.status_code == 204


def test_default(respx_mock):
    respx_mock.get("http://0.0.0.0:8000/").mock(return_value=httpx.Response(204))
    response = httpx.get("http://0.0.0.0:8000/")
    assert response.status_code == 204


@pytest.mark.respx(base_url="http://0.0.0.0:8000/")
def test_with_marker(respx_mock):
    respx_mock.get("/baz/").mock(return_value=httpx.Response(204))
    response = httpx.get("http://0.0.0.0:8000/weather/Moscow")
    assert response.status_code == 204
