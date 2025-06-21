from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero.app import app


def test_root_deve_retornar_ola_mundo():
    """test of triple A (aaa): arrange / act / assert"""

    client = TestClient(app)  # arrange

    response = client.get('/')  # act

    assert response.json() == {'message': 'Olá, mundo!'}  # assert
    assert response.status_code == HTTPStatus.OK
