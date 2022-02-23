import os


def start_terminal(connection):
    user_input = ""

    while user_input != "quit":
        user_input = input(">> ")
        connection.sendall(str.encode(user_input))
