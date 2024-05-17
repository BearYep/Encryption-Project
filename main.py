from Encryption import CipherMachine

app = CipherMachine()

def main():
    while True:
        mode = input('Please insert the mode you want: 1(Encode), 2(Decode):  (1/2) ')
        if(mode == '1'):
            plain_text = input('Pleas insert the plain text: ')
            key = input('Please insert the key: ')
            app.encode(plain_text, key)
        elif(mode == '2'):
            cipher_text = input('Pleas insert the cipher text: ')
            key = input('Please insert the key: ')
            app.decode(cipher_text, key)
        else:
            print('Wrong Mode!')
            break
    
if __name__ == "__main__":
    main()