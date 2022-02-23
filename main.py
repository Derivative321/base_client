import socket

from login import handle_login
from user_creation import user_creation

client_socket = socket.socket()
host = '127.0.0.1'
port = 1234


def grand_base_controller(connection):
    user_input = input("Are you a new user (y/n): ")

    if user_input == "y":
        connection.sendall(str.encode("new-user"))
        user_creation(connection)
    elif user_input == "n":
        handle_login(connection)


try:
    client_socket.connect((host, port))
    while True:
        grand_base_controller(client_socket)
    client_socket.close()
except socket.error as e:
    print(str(e))


