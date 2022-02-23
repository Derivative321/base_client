import re


def get_and_validate_username(connection):
    username = input("Please enter a username:\n")
    connection.sendall(str.encode(username))
    response = connection.recv(1024).decode("utf-8")
    while response == "invalid":
        username = input("That username is already taken, please try another:\n")
        connection.sendall(str.encode(username))
        response = connection.recv(1024).decode("utf-8")


def get_and_validate_email(connection):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    email = input("Please enter a valid email:\n")
    if not re.fullmatch(regex, email):
        email = input("Email must in format (name@website.com):\n")
    connection.sendall(str.encode(email))
    response = connection.recv(1024).decode("utf-8")
    while response == "invalid":
        email = input("That email is already in use, please try another:\n")
        if not re.fullmatch(regex, email):
            email = input("Email must in format (name@website.com):\n")
        connection.sendall(str.encode(email))
        response = connection.recv(1024).decode("utf-8")


def get_and_validate_password(connection):
    password = input("Please enter your desired password:\n")
    validate_password = input("Please validate your password:\n")
    while password != validate_password:
        print("Passwords don't match, please try again.")
        password = input("Please enter your desired password:\n")
        validate_password = input("Please validate your password:\n")
    connection.sendall(str.encode(password))


def user_creation(connection):
    get_and_validate_username(connection)
    get_and_validate_email(connection)
    get_and_validate_password(connection)
