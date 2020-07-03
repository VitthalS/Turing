#-*- coding: utf-8 -*-


import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS).encode()
unpad = lambda s: s[:-ord(s[len(s)-1:])]
iv = 'a1b2c3d4e5f6g7h8'


class AESCipher(object):
   

    def __init__(self, key):
    	
    	self.key = key
        

    def encrypt(self, message):
        
        message = message.encode()
        raw = pad(message)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        enc = cipher.encrypt(raw)
        return base64.b64encode(enc).decode('utf-8')

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        dec = cipher.decrypt(enc)
        return unpad(dec).decode('utf-8')


key = 'a1b2c3d4e5f6g7h8'

message = input()

enc = AESCipher(key).encrypt(message)
#dec = AESCipher(key).decrypt(_enc)


print(enc)
#print(dec)
