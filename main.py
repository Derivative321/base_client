import socket

from login import handle_login
from user_creation import user_creation

connection = socket.socket()
host = "127.0.0.1"
port = 1234


def grand_base_controller():
    user_input = input("Are you a new user (yes/no): ")

    if user_input.lower() == "yes":
        connection.sendall(str.encode("new-user"))
        user_creation(connection)
    elif user_input.lower() == "no":
        handle_login(connection)


try:
    connection.connect((host, port))
    while True:
        grand_base_controller()
except socket.error as e:
    print(str(e))


