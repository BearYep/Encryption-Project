
import Encryption.webC as webC
from Encryption.rrr import RRR
import Encryption.rotate as rotate
import Encryption.braille_cipher as braille
from Encryption.FibraEncryption_final import FibraEncryption
from Encryption.one_connect import one_con

rrr = RRR()
Fibra = FibraEncryption()
oneCon = one_con()

class CipherMachine:
    def __init__(self):
        pass
    
    def encode(self, plain_text = None, key = None):
        cipher_text = webC.fold_and_encrypt(plain_text, key)
        cipher_text = rrr.encode(cipher_text, key)
        cipher_text = rotate.encode(cipher_text, key)
        cipher_text = braille.encode(cipher_text, key)
        cipher_text = Fibra.encrypt(cipher_text, key)
        cipher_text = oneCon.encrypt(cipher_text, key)
        
        return cipher_text
        
    def decode(self, cipher_text = None, key = None):
        plain_text = oneCon.decrypt(cipher_text, key)
        plain_text = Fibra.decrypt(plain_text, key)
        plain_text = braille.decode(plain_text, key)
        plain_text = rotate.decode(plain_text, key)
        plain_text = rrr.decode(plain_text, key)
        plain_text = webC.decrypt_and_unfold(plain_text, key)

        return plain_text