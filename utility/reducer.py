import json

from utility.const import ACTIONS
from utility.contacts.crud import add_contact, del_contact, get_contacts
from utility.db.models import User
from utility.utility import user_authenticate, user_presens, user_message


def sort_mess(sockets):

    for socket in sockets:
        data = socket.recv(1024).decode('utf-8')
        data = json.loads(data)
        if data["action"] == ACTIONS["presence"]:
            user_presens(socket, data)
        elif data["action"] == ACTIONS["msg"]:
            user_message(socket)
        elif data["action"] == ACTIONS["authenticate"]:
            user_authenticate(socket, data)
        elif data["action"] == ACTIONS["add_contact"]:
            add_contact(socket,data)
        elif data["action"] == ACTIONS["del_contact"]:
            del_contact(socket,data)
        elif data["action"] == ACTIONS["get_contacts"]:
            get_contacts(socket)
