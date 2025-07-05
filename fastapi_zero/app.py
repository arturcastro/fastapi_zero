from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fastapi_zero.schemas import Message

app = FastAPI(title='Books API')


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return Message(message='Olá, mundo!')
    # return {'message': 'Olá, mundo!'}


@app.get('/html-hi', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def exercise():
    return '<h2>Olá, mundo!</h2>'
