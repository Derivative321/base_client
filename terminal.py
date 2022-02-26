from user_creation import *


def start_terminal(connection):
    command = ""

    while command != "quit":
        command = input(">> ")
        commands(connection, command)


def commands(connection, command):
    if command == "passwd":
        connection.sendall(str.encode(command))
        current_password = input("Please validate you current password: ")
        connection.sendall(str.encode(current_password))
        response = connection.recv(1024)
        if response == "valid":
            get_and_validate_password(connection)
            # FINISH

