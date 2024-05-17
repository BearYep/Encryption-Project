from Encryption import CipherMachine

app = CipherMachine()

def main():
    while True:
        mode = input('Please insert the mode you want: 1(Encode), 2(Decode):  (1/2) ')
        if(mode == '1'):
            plain_text = input('Pleas insert the plain text: ')
            key = input('Please insert the key: ')
            cipher_text = app.encode(plain_text, key)
            print(f'明文 : {plain_text} ; Key: {key} ; 密文 : {cipher_text}')
        elif(mode == '2'):
            cipher_text = input('Pleas insert the cipher text: ')
            key = input('Please insert the key: ')
            plain_text = app.decode(cipher_text, key)
            print(f'密文 : {cipher_text} ; Key: {key} ; 密文 : {plain_text}')
        elif(mode == '3'):
            #驗證用
            plain_text = input('Pleas insert the plain text: ')
            key = input('Please insert the key: ')
            cipher_text = app.encode(plain_text, key)
            print(f'明文 : {plain_text} ; Key: {key} ; 密文 : {cipher_text}')
            
            plain_text = app.decode(cipher_text, key)
            print(f'密文 : {cipher_text} ; Key: {key} ; 明文 : {plain_text}')
        else:
            print('Wrong Mode!')
            break
    
if __name__ == "__main__":
    main()