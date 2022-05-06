"""Программа клиента, отправляющего/читающего простые текстовые сообщения на сервер"""
import json
from socket import socket, AF_INET, SOCK_STREAM

from utility.const import PORT, HOST, ACTIONS
from utility.db.models import User
from utility.jim_settings.msg_obj import MsgObj
from utility.utility import auth_mess, presens_mess


def echo_client():
    """Общение с сервером"""
    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        # account_name = input("Введите свой аккаунт: ")
        # presens_mess(sock, account_name)
        # auth_mess(sock, account_name)
        while True:
            # Сообщение не должно состоять из пустой строки или пробелов
            msg = ''
            while msg.strip() == '':
                msg = input('Для команд наберите:'
                            '\nexit- что бы выйти'
                            '\nC - посмотреть все контакты '
                            '\nadd - Добавить контакт'
                            '\ndel - Удалить контакт'
                            '\nВвод: ')
            if msg == 'exit':
                break
            elif msg == 'C':
                msg = MsgObj(ACTIONS['get_contacts'])
                sock.send(msg())
                data = sock.recv(1024).decode('utf-8')
                data = json.loads(data)
                if data["response"] == 200:
                    for client in data["alert"]:
                        print(client)
            elif msg == 'add':
                login = input('Введите логин: ')
                info = input('Введите инфо: ')
                password = input('Введите пароль: ')
                user = {
                    'login': login,
                    'info': info,
                    'password': password
                }
                msg = MsgObj(ACTIONS['add_contact'], user=user)
                sock.send(msg())
                data = sock.recv(1024).decode('utf-8')
                data = json.loads(data)
                print(f'{data["response"]}. {data["alert"]}')
            elif msg == 'del':
                id = input('Введите id клиента, которого хотите удалить: ')
                msg = MsgObj(ACTIONS['del_contact'], id=id)
                sock.send(msg())
                data = sock.recv(1024).decode('utf-8')
                data = json.loads(data)
                print(f'{data["response"]}. {data["alert"]}')


if __name__ == '__main__':
    echo_client()
