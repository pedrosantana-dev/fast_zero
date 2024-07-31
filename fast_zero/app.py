from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message, UserPublic, UserSchema

app = FastAPI()


@app.get("/", status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {"message": "Olá, mundo!"}


@app.get("/olamundo", status_code=HTTPStatus.OK, response_class=HTMLResponse)
def ola_mundo_html():
    return """
    <html>
        <head>
            <title>Olá, mundo!</title>
        </head>
        <body>
            <h1>Olá, mundo!</h1>
        </body>
    </html>
    """


@app.post("/users", status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    return user
