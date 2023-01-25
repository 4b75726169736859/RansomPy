from cryptography.fernet import Fernet
import os
import win32api


def decrypt(thisKey, thisFolder):
    fernet = Fernet(thisKey)
    for path, subdirs, files in os.walk(thisFolder):
        for name in files:
            try:
                tempTuple = os.path.splitext(os.path.join(path, name))
                filename = tempTuple[0]
                os.rename(os.path.join(path, name), filename)
                with open(filename, 'rb') as enc_file:
                    encrypted = enc_file.read()
                decrypted = fernet.decrypt(encrypted)
                with open(filename, 'wb') as dec_file:
                    dec_file.write(decrypted)
            except:
                pass
    win32api.MessageBox(0, 'Vos fichier on bien ete decrypter', 'Encrypt', 0x00001000)


if __name__ == '__main__':
    key = input('Entrez la clé de decryptage : ')
    decrypt(key, 'test')
