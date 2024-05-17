import Encryption.braille_cipher as braille
import Encryption.webC as webC
from Encryption.rrr import RRR
from Encryption.FibraEncryption_final import FibraEncryption
from Encryption.one_connect import one_con

rrr = RRR()
Fibra = FibraEncryption()
oneCon = one_con()

class CipherMachine:
    def __init__(self):
        pass
    
    def encode(self, plain_text = None, key = None):
        
        cipher_text1 = webC.fold_and_encrypt(plain_text, key)
        cipher_text2 = rrr.encode(cipher_text1, key)
        #cipher_text3 = 林柏榕==
        cipher_text3 = braille.encode(cipher_text2, key)
        cipher_text4 = Fibra.encrypt(cipher_text3, key)
        cipher_text5 = oneCon.encrypt(cipher_text4, key)
        
        return cipher_text5
        
    def decode(self, cipher_text = None, key = None):

        plain_text1 = oneCon.decrypt(cipher_text, key)
        plain_text2 = Fibra.decrypt(plain_text1, key)
        plain_text3 = braille.decode(plain_text2, key)
        #plain_text4 = 林柏榕==
        plain_text4 = rrr.decode(plain_text3, key)
        plain_text5 = webC.decrypt_and_unfold(plain_text4, key)
        
        return plain_text5