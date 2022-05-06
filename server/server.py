from select import select
from socket import socket, AF_INET, SOCK_STREAM
from utility.const import PORT
from utility.reducer import sort_mess



def mainloop():
    """Основной цикл обработки запросов клиентов"""

    address = ('', PORT)
    all_clients = []

    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.bind(address)
        sock.listen(5)
        sock.settimeout(2)
        while True:
            try:
                conn, addr = sock.accept()
            except OSError as err:
                pass
            else:
                print(f"Получен запрос на соединение от {str(addr)}")
                all_clients.append(conn)
            finally:
                wait = 0
                senders=[]
                connected = []
                try:
                    senders, connected, errors = select(all_clients, all_clients, [], wait)

                    if senders:
                        sort_mess(senders)
                except Exception as e:
                    print(e)


mainloop()
