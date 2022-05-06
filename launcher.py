import subprocess
from subprocess import CREATE_NEW_CONSOLE


def launcher():
    process_list = []
    while True:
        user = input('Введите s - для запуска сервера, q - что бы выйти: ').lower()
        if user == 'q':
            break

        server = subprocess.Popen(['python', 'server\\server.py'], creationflags=CREATE_NEW_CONSOLE)
        client1 = subprocess.Popen(['python', 'client\\client.py'], creationflags=CREATE_NEW_CONSOLE)
        client2 = subprocess.Popen(['python', 'client\\client.py'], creationflags=CREATE_NEW_CONSOLE)
