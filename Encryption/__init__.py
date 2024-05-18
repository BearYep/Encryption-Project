
import Encryption.webC as webC
from Encryption.rrr import RRR
import Encryption.rotate as rotate
import Encryption.braille_cipher as braille
from Encryption.FibraEncryption_final import FibraEncryption
from Encryption.one_connect import one_con

import random
import os

rrr = RRR()
Fibra = FibraEncryption()
oneCon = one_con()

class CipherMachine:
    def __init__(self):
        self.random_times = 100
        self.information_flag = False
    
    def encode(self, plain_text = None, key = None, test_flag = False):
        if(not test_flag):
            plain_text = input('Please insert the plain text: ')
            key = input('Please insert the key: ')
        
        cipher_text = webC.fold_and_encrypt(plain_text, key)
        cipher_text = rrr.encode(cipher_text, key)
        cipher_text = rotate.encode(cipher_text, key)
        cipher_text = braille.encode(cipher_text, key)
        cipher_text = Fibra.encrypt(cipher_text, key)
        cipher_text = oneCon.encrypt(cipher_text, key)

        if(not test_flag):
            print(f'明文 : {plain_text} ; Key: {key} ; 密文 : {cipher_text}')
        return cipher_text
        
    def decode(self, cipher_text = None, key = None, test_flag = False):
        if(not test_flag):
            cipher_text = input('Please insert the cipher text: ')
            key = input('Please insert the key: ')
            
        plain_text = oneCon.decrypt(cipher_text, key)
        plain_text = Fibra.decrypt(plain_text, key)
        plain_text = braille.decode(plain_text, key)
        plain_text = rotate.decode(plain_text, key)
        plain_text = rrr.decode(plain_text, key)
        plain_text = webC.decrypt_and_unfold(plain_text, key)
        
        if(not test_flag):
            print(f'密文 : {cipher_text} ; Key: {key} ; 明文 : {plain_text}')
        return plain_text
    
    def test(self):
        plain_text = input('Please insert the plain text: ')
        key = input('Please insert the key: ')
        
        cipher_text = self.encode(plain_text, key, True)
        print(f'明文 : {plain_text} ; Key: {key} ; 密文 : {cipher_text}')
        decrypted_text = self.decode(cipher_text, key, True)
        print(f'密文 : {cipher_text} ; Key: {key} ; 明文 : {plain_text}')
        
        if decrypted_text != plain_text:
            print("Decryption error!")
            print("Key:", key)
            print("Plaintext:", plain_text)
            print("Cipher text:", cipher_text)
            print("Decrypted_text:", decrypted_text)
            os.system('pause')
            print("------------------------")
        else:
            print("Decryption pass!")
            if self.information_flag:
                print("Key:", key)
                print("Plaintext:", plain_text)
                print("Cipher text:", cipher_text)
                print("Decrypted_text:", decrypted_text)
                print("------------------------")
        
    def random_test(self):
        #隨機生成固定長度5的明文，以及長度<=5的key進行加密並解密，驗證原明文是否與解密後明文相等
        for _ in range(self.random_times):
            length = 5
            key = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k = length))

            length = random.randint(1, 100)
            plain_text = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k = length))
            # Encrypt
            cipher_text = self.encode(plain_text, key, True)

            # Decrypt
            decrypted_text = self.decode(cipher_text, key, True)

            # Check if decryption result matches plaintext
            if decrypted_text != plain_text:
                print("Decryption error!")
                print("Key:", key)
                print("Plaintext:", plain_text)
                print("Cipher text:", cipher_text)
                print("Decrypted_text:", decrypted_text)
                os.system('pause')
                print("------------------------")
            else:
                print("Decryption pass!")
                if self.information_flag:
                    print("Key:", key)
                    print("Plaintext:", plain_text)
                    print("Cipher text:", cipher_text)
                    print("Decrypted_text:", decrypted_text)
                    print("------------------------")