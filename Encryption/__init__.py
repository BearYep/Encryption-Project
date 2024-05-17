
import Encryption.webC as webC
from Encryption.rrr import RRR
import Encryption.rotate as rotate
import Encryption.braille_cipher as braille
from Encryption.FibraEncryption_final import FibraEncryption
from Encryption.one_connect import one_con

import random

rrr = RRR()
Fibra = FibraEncryption()
oneCon = one_con()

class CipherMachine:
    def __init__(self):
        self.random_times = 100
        self.information_flag = False
    
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
    
    def random_test(self):
        for _ in range(self.random_times):
            length = random.randint(1,5)
            key = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k = length))

            length = 5
            plaintext = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k = length))
            # Encrypt
            cipher_text = self.encode(plaintext, key)

            # Decrypt
            decrypted_text = self.decode(cipher_text, key)

            # Check if decryption result matches plaintext
            if decrypted_text != plaintext:
                print("Decryption error!")
                print("Key:", key)
                print("Plaintext:", plaintext)
                print("Cipher text:", cipher_text)
                print("Decrypted_text:", decrypted_text)
                print("------------------------")
            else:
                print("Decryption pass!")
                if self.information_flag:
                    print("Key:", key)
                    print("Plaintext:", plaintext)
                    print("Cipher text:", cipher_text)
                    print("Decrypted_text:", decrypted_text)
                    print("------------------------")