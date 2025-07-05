from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero.app import app


def test_root_deve_retornar_ola_mundo():
    """test of triple A (aaa): arrange / act / assert"""

    client = TestClient(app)  # arrange

    response = client.get('/')  # act

    assert response.json() == {'message': 'Olá, mundo!'}  # assert
    assert response.status_code == HTTPStatus.OK


def test_exercise_deve_retornar_ola_mundo_em_HTML():
    client = TestClient(app)
    response = client.get('/html-hi')
    assert response.text == '<h2>Olá, mundo!</h2>'
    assert response.status_code == HTTPStatus.OK
