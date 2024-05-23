
import Encryption.webC as webC
from Encryption.rrr import RRR
import Encryption.rotate as rotate
import Encryption.braille_cipher as braille
from Encryption.FibraEncryption_final2 import FibraEncryption
from Encryption.one_connect import one_con

import random
import os
import hashlib

rrr = RRR()
Fibra = FibraEncryption()
oneCon = one_con()


class CipherMachine:
    def __init__(self):
        self.random_times = 100000
        self.information_flag = False
    
    def encode(self, plain_text = None, key = None, test_flag = False):
        if(not test_flag):
            plain_text = input('Please insert the plain text: ')
            key = input('Please insert the key: ')
        
        origin_key = key
        key = self.extend_key(key)
        cipher_text1 = webC.fold_and_encrypt(plain_text, key)
        cipher_text2 = rrr.encode(cipher_text1, key)
        cipher_text3 = rotate.encode(cipher_text2, key)
        cipher_text4 = braille.encode(cipher_text3, key)
        cipher_text5 = Fibra.encrypt(cipher_text4, key)
        cipher_text6 = oneCon.encrypt(cipher_text5, key)

        if(self.information_flag):
            print(f'==============================加密各步驟分析==================================')
            print(f'Key:{origin_key}')
            print(f'(1) 明文  : {plain_text} -> 密文1 : {cipher_text1}')
            print(f'(2) 密文1 : {cipher_text1} -> 密文2 : {cipher_text2}')
            print(f'(3) 密文2 : {cipher_text2} -> 密文3 : {cipher_text3}')
            print(f'(4) 密文3 : {cipher_text3} -> 密文4 : {cipher_text4}')
            print(f'(5) 密文4 : {cipher_text4} -> 密文5 : {cipher_text5}')
            print(f'(6) 密文5 : {cipher_text5} -> 最終密文 : {cipher_text6}')
                
        if(not test_flag):
            print(f'=================================加密結果=====================================')
            print(f'明文 : {plain_text} ; Key: {origin_key} ; 密文 : {cipher_text6}')
        return cipher_text6
        
    def decode(self, cipher_text = None, key = None, test_flag = False):
        if(not test_flag):
            cipher_text = input('Please insert the cipher text: ')
            key = input('Please insert the key: ')
        
        origin_key = key
        key = self.extend_key(key)
        plain_text1 = oneCon.decrypt(cipher_text, key)
        plain_text2 = Fibra.decrypt(plain_text1, key)
        plain_text3 = braille.decode(plain_text2, key)
        plain_text4 = rotate.decode(plain_text3, key)
        plain_text5 = rrr.decode(plain_text4, key)
        plain_text6 = webC.decrypt_and_unfold(plain_text5, key)
        
        if(self.information_flag):
            print(f'==============================解密各步驟分析==================================')
            print(f'Key:{origin_key}')
            print(f'(1) 密文  : {cipher_text} -> 明文1 : {plain_text1}')
            print(f'(2) 明文1 : {plain_text1} -> 明文2 : {plain_text2}')
            print(f'(3) 明文2 : {plain_text2} -> 明文3 : {plain_text3}')
            print(f'(4) 明文3 : {plain_text3} -> 明文4 : {plain_text4}')
            print(f'(5) 明文4 : {plain_text4} -> 明文5 : {plain_text5}')
            print(f'(6) 明文5 : {plain_text5} -> 最終明文 : {plain_text6}')
            
        if(not test_flag):
            print(f'=================================解密結果=====================================')
            print(f'密文 : {cipher_text} ; Key: {origin_key} ; 明文 : {plain_text6}')
        return plain_text6
    
    def test(self):
        plain_text = input('Please insert the plain text: ')
        key = input('Please insert the key: ')
        
        cipher_text = self.encode(plain_text, key, True)
        print(f'=================================加密結果=====================================')
        print(f'明文 : {plain_text} ; Key: {key} ; 密文 : {cipher_text}')
        print(f'\n')
        decrypted_text = self.decode(cipher_text, key, True)
        print(f'=================================解密結果=====================================')
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
        
    def random_test(self):
        #隨機生成固定長度5的明文，以及長度<=5的key進行加密並解密，驗證原明文是否與解密後明文相等
        for _ in range(self.random_times):
            length = random.randint(1, 100)
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

                    
    def extend_key(self, key:str):
        if len(key) > 30:
            key = key[:30]
            return key
        s= hashlib.sha256()
        s.update(key.encode("utf-8"))
        hash_key = s.hexdigest()

        if len(hash_key) >= 30:
            key = hash_key

        while len(hash_key) < 30:
            key = key + hash_key
        
        key = key[:30]
        return str(key)