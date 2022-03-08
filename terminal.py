from user_creation import *


def start_terminal(connection):
    command = ""

    while command != "quit":
        command = input(">> ")
        commands(connection, command)


def commands(connection, command):
    if command == "passwd":
        connection.sendall(str.encode(command))
        response = ""
        while response != "valid":
            current_password = input("Please validate you current password: ")
            connection.sendall(str.encode(current_password))
            response = connection.recv(1024).decode("utf-8")
        else:
            get_and_validate_password(connection)

