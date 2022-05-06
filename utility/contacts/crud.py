from sqlalchemy import select
from socket import socket
from utility.db.models import User
from utility.db.session import get_session
from utility.jim_settings.response import RespObj


def add_contact(socket: socket, data: dict) -> None:
    session = get_session()
    user = data['user']
    new_user = User(**user)
    try:
        session.add(new_user)
        session.commit()
    except Exception as er:
        resp = RespObj(alert=er)
        socket.send(resp())
        return
    resp = RespObj(alert="Контакт добавлен")
    socket.send(resp())


def del_contact(socket: socket, data: dict) -> None:
    session = get_session()
    try:
        session.query(User).filter(User.id == data['id']).delete()
        session.commit()
        resp = RespObj(alert="Контакт удален")
    except Exception as er:
        resp = RespObj(alert=er)
    socket.send(resp())


def get_contacts(socket: socket) -> list[object]:
    session = get_session()
    items = select(User)
    result = session.execute(items)
    result = [x[0].to_dict() for x in result]
    resp = RespObj(alert=result)
    socket.send(resp())
    return result
