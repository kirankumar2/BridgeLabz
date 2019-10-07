import os
import base64


def secure_rand(len=6):
    token = os.urandom(len)
    print(base64.b64encode(token))


secure_rand()
