import json
from socket import socket

from sqlalchemy.orm import Session


from utility.jim_settings.msg_obj import MsgObj
from utility.jim_settings.response import RespObj


def auth_mess(sock: socket, account_name) -> None:
    while True:
        password = input("Введите пароль: ")
        user = {
            "account_name": account_name,
            "password": password
        }
        mess = MsgObj('authenticate', user=user)
        sock.send(mess())
        resp_from_server = sock.recv(1024).decode('utf-8')
        resp_from_server = json.loads(resp_from_server)

        if resp_from_server['response'] == 200:
            print("Вы авторизованны")
            break
        else:
            print(resp_from_server['alert'])


def user_authenticate(sock: socket, data: dict) -> None:
    user = data["user"]
    if user["account_name"] == "messi" and str(user["password"]) == "1234":
        resp = RespObj()
        sock.send(resp())
    else:
        resp = RespObj(111, 'Incorrect username or password')
        sock.send(resp())


def presens_mess(sock: socket, account_name) -> None:
    user = {
        "account_name": account_name,
        "status": "User is online"
    }
    pres_mess = MsgObj('presence', user=user)
    sock.send(pres_mess())
    resp_from_server = sock.recv(1024).decode('utf-8')
    resp_from_server = json.loads(resp_from_server)
    if resp_from_server['response'] == 200:
        print(f"Добро пожаловать в чат {account_name}")
    else:
        print(resp_from_server['alert'])


def user_presens(sock: socket, data: dict) -> None:
    # user=data["user"]
    resp = RespObj()
    sock.send(resp())


def send_message(sock):
    pass


def user_message(sock):
    pass



# def db_session() -> Session:
#     db=None
#     try:
#         db=SessionLocal()
#         yield db
#     finally:
#         if db is not None:
#             db.close()