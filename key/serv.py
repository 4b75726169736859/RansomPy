from cryptography.fernet import Fernet
from sys import stdout, exit
from time import time


if __name__ == '__main__':
    k = Fernet.generate_key()
    f = open("key/" + str(int(time())) + ".txt", "w")
    f.write(str(k.decode()))
    f.close()

    stdout.write(str(k.decode()))
    exit(0)