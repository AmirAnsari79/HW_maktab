from cryptography.fernet import Fernet

# A
key = Fernet.generate_key()
with open('A.txt', 'w') as f:
    f.write(str(Fernet(key)))


# B
# f = Fernet(key)
# text = f.encrypt(b"my deep dark secret")

def mydec(func):
    def wrapper(*args, **kwargs):
        temp = func(*args, **kwargs)
        key = Fernet.generate_key()
        f = Fernet(key)
        text = f.encrypt(temp)
        return text

    return wrapper


class Encrypt:
    def __init__(self):
        pass

    def encrypt(self, token):
        key = Fernet.generate_key()
        f = Fernet(key)
        text = f.encrypt(token)
        return text

    def decrpt(self, key, text):
        f = Fernet(key)
        print(f.decrypt(text))

    @mydec
    def myfunc(self, *args):
        pass


d = Encrypt()
d.decrpt(b'60dAdxTee1NjnvH-g2-eCNffrJMay48fQKekD65cT34=',
         b'gAAAAABgvKlvwfQMHuIqjsXH_TGQQqXBqC0tFiPBdVQxvtqMdzrW6ji3f3YwdTVsmXCZVGaJiLS1aqABhuIW77TlxgWfgkAidAij1zcTwZLWg4bMaHhxKdE=')
#
print(d.encrypt(b'amir'))


# C


class Decrypt:
    def decrpt(self, key, text):
        f = Fernet(key)
        print(f.decrypt(text))
