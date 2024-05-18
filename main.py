from Encryption import CipherMachine

app = CipherMachine()

def main():
    while True:
        mode = input('Please insert the mode you want: 1(Encode), 2(Decode):  (1/2) ')
        if(mode == '1'):
            app.encode()
        elif(mode == '2'):
            app.decode()
        elif(mode == '3'):
            #驗證用
            app.test()
        elif(mode == '4'):
            app.random_test()
        else:
            print('Wrong Mode!')
            break
    
if __name__ == "__main__":
    main()