import Encryption.braille_cipher as braille

class CipherMachine:
    def __init__(self):
        pass
    
    def encode(self, plain_text = None, key = None):
        cipher_text = braille.encode(plain_text, key)
        
        return cipher_text
        
    def decode(self, cipher_text = None, key = None):
        plain_text = braille.decode(cipher_text, key)
        
        return plain_text