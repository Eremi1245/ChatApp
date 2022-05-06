ACTIONS = {
    "presence": "presence",  # — присутствие. Сервисное сообщение для
    # извещения сервера о присутствии клиента online;
    "prоbe": "prоbe",  # — проверка присутствия.
    # Сервисное сообщение от сервера для проверки присутствии клиента online;
    "msg": "msg",  # — простое сообщение пользователю или в чат;
    "quit": "quit",  # — отключение от сервера;
    "authenticate": "authenticate",  # — авторизация на сервере;
    "join": "join",  # — присоединиться к чату;
    "leave": "leave",  # — покинуть чат.
    "add_contact": "add_contact",
    "del_contact": "del_contact",
    "get_contacts": "get_contacts"
}

PORT = 8008
HOST = 'localhost'
CONNECT_TO_DB='mysql+pymysql://root:1234@localhost/python_chat'