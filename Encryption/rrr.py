class RRR:
    def __init__(self):
        self.matrix = []
        self.matrix = [["" for _ in range(6)] for _ in range(6)]
        self.reserved = []
        self.reverse = False
        self.padding = False

    def generate_reverse_matrix(self, key):

        alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
        key_set = set(key)
        exited = []

        for letter in self.reserved:
            if letter not in exited:
                exited.append(letter)
       
        for i in range(6):
            for j in range(6):
                if self.matrix[5-i if self.reverse else i][5-j if self.reverse else j] not in self.reserved:
                    self.matrix[5-i if self.reverse else i][5-j if self.reverse else j] = ""

        for letter in key:
            if letter not in exited:
                filled = False
                for i in range(6):
                    for j in range(6):
                        if self.matrix[5-i if self.reverse else i][5-j if self.reverse else j] == "":
                            self.matrix[5-i if self.reverse else i][5-j if self.reverse else j] = letter
                            exited.append(letter)
                            filled = True
                            break
                    if filled:
                        break
                   
        for letter in alphabet:
            if letter not in exited:
                filled = False
                for i in range(6):
                    for j in range(6):
                        if self.matrix[5-i if self.reverse else i][5-j if self.reverse else j] == "":
                            self.matrix[5-i if self.reverse else i][5-j if self.reverse else j] = letter
                            exited.append(letter)
                            filled = True
                            break
                    if filled:
                        break
              
        self.reverse = not self.reverse
        return self.matrix

    def find_position(self, matrix, letter):
        #印出matrix
        for i in range(6):
            for j in range(6):
                print(matrix[i][j], end=" ")
            print()
        for i in range(6):
            for j in range(6):
                if matrix[i][j] == letter:
                    return i, j

    def encode(self, plaintext, key):
        martix = self.generate_reverse_matrix(key)
        ciphertext = ""
        plaintext += "X" * (len(plaintext) % 2)

        for i in range(0, len(plaintext), 2):
            pair = plaintext[i:i+2]
            if pair[1] == "X":
                self.padding = True
                pair = pair[0] + "x"
            self.reserved.append(pair[0])
            self.reserved.append(pair[1])
            print(pair)
            row1, col1 = self.find_position(martix, pair[0])
            row2, col2 = self.find_position(martix, pair[1])

            if row1 == row2 and col1 == col2:
                if self.reverse:
                    ciphertext += martix[row1][(col1+1)%6] + martix[row2][(col2+1)%6]
                else:
                    ciphertext += martix[row1][(col1-1)%6] + martix[row2][(col2-1)%6]
            elif row1 == row2:
                if self.reverse:
                    ciphertext += martix[(row1+1)%6][col1] + martix[(row2+1)%6][col2]
                else:
                    ciphertext += martix[(row1-1)%6][col1] + martix[(row2-1)%6][col2]
            elif col1 == col2:
                if self.reverse:
                    ciphertext += martix[row1][(col1+1)%6] + martix[row2][(col2+1)%6]
                else:
                    ciphertext += martix[row1][(col1-1)%6] + martix[row2][(col2-1)%6]
            else:
                ciphertext += martix[row1][col2] + martix[row2][col1]
            print("密文:",ciphertext)
            print()

            martix = self.generate_reverse_matrix(key)
            
            for i in range(6):
                for j in range(6):
                    print(martix[i][j],end=" ")
                print()
            print() 

        if self.padding:
            ciphertext = ciphertext[:-1] + ciphertext[-1].upper()
        self.padding = False
        return ciphertext
    

    def decode(self, ciphertext, key):
        self.reserved = []
        self.reverse = False
        #生成playfair密碼矩陣
        martix = self.generate_reverse_matrix(key)

        for i in range(6):
            for j in range(6):
                print(martix[i][j],end=" ")
            print()

        print()
        #將密文分組並解密
        plaintext = ""
        for i in range(0,len(ciphertext),2): #將密文分組
            pair=ciphertext[i:i+2] #取出一組
            if(pair[1].isupper()): 
                self.padding=True
                pair=pair[0]+pair[1].lower()

            row1,col1=self.find_position(martix,pair[0])
            row2,col2=self.find_position(martix,pair[1])
              
            if row1==row2 and col1==col2: #如果兩個字母相同，密文取該字母右邊的字母
                if(self.reverse):
                    plaintext+=martix[row1][(col1-1)%6]+martix[row2][(col2-1)%6]
                else:
                    plaintext+=martix[row1][(col1+1)%6]+martix[row2][(col2+1)%6]
            elif row1==row2:
                if(self.reverse):
                    plaintext+=martix[(row1-1)%6][col1]+martix[(row2-1)%6][col2]
                else:
                    plaintext+=martix[(row1+1)%6][col1]+martix[(row2+1)%6][col2]
            elif col1==col2:
                if(self.reverse):
                    plaintext+=martix[row1][(col1-1)%6]+martix[row2][(col2-1)%6]
                else:
                    plaintext+=martix[row1][(col1+1)%6]+martix[row2][(col2+1)%6]
            else:
                plaintext+=martix[row1][col2]+martix[row2][col1]

            print("解密後的明文為:",plaintext)
            print()
            #把解出來的明文加進reserved列表中
            self.reserved.append(plaintext[-2])
            self.reserved.append(plaintext[-1])
            print(self.reserved)

            martix = self.generate_reverse_matrix(key)
            #印出矩陣
            for i in range(6):
                for j in range(6):
                    print(martix[i][j],end=" ")
                print()
            print()
        #若padding為True，則最後一個字母刪除
        if self.padding:
            plaintext=plaintext[:-1]
        self.padding = False
        return plaintext
    
    def main(self):
        PlainText = input("請輸入明文:")
        PlainText = PlainText.replace(" ", "")
        key = input("請輸入密鑰:")
        CipherText = self.encode(PlainText, key)
        print("加密後的密文為:", CipherText)

        CipherText = input("請輸入密文:")
        key=input("請輸入密鑰:")
        PlainText = self.decode(CipherText,key)

        print("解密後的明文為:",PlainText)


if __name__ == "__main__":
    rrr = RRR()
    rrr.main()