from terminal import start_terminal


def handle_login(connection):
    print("Please enter your username or email and password")
    username = input("Username: ")
    password = input("Password: ")
    connection.sendall(str.encode(username))
    connection.sendall(str.encode(password))

    response = connection.recv(1024).decode("utf-8")
    if response == "success":
        start_terminal(connection)

