class one_con():
    def __init__(self):
        self.key = ""
        self.plain_text = ""
        self.cipher_text = []
        self.binary_key = []
        self.binary_message = []
    def set_key(self,key):
        self.key = key
    def set_plain_text(self,plain_text):
        self.plain_text = plain_text
    def set_cipher_text(self,cipher_text):
        self.cipher_text = cipher_text
    def get_plain_text(self):
        return self.plain_text
    def get_cipher_text(self):
        return self.cipher_text
    def get_binary_key(self):
        return self.binary_key
    def get_binary_message(self):
        return self.binary_message
    
    def convert_key(self):
        kb = []
        for i in self.key:
            if ord(i)<=57: 
                k = format(ord(i) - 47, '06b') 
            elif i.isupper(): 
                k = format(ord(i) - 54, '06b')
            else:
                k = format(ord(i) - 60, '06b')
            kb.append(k)
        if len(self.key)<5:
            s=0
            for i in range(5-len(self.key)):
                kb.append(kb[s])
                s+=1
        return kb

    def convert_message(self):
        b_message = []
        for i in self.plain_text:
            if ord(i)<=57: 
                k = format(ord(i) - 47, '06b') 
            elif i.isupper(): 
                k = format(ord(i) - 54, '06b')
            else:
                k = format(ord(i) - 60, '06b')
            b_message.append(k)
        self.binary_message = b_message

    def encrypt(self,plain_text,key):
        self.set_key(key)
        self.set_plain_text(plain_text)
        self.binary_key = self.convert_key()
        self.convert_message()
        cipher_text = []
        for i in self.binary_message:
            Calculate = []
            one_site = []
            for k in range(6):
                    if i[k] == "1":
                        one_site.append(k)
            round = 0
            key_round=0
            for j in self.binary_key:
                one_index = j.find("1")
                for r in range(2):
                    if one_site[round]>one_index:
                        Calculate.append(((((one_site[round]-one_index)**2+1)**0.5) / 10)* 2**(5+key_round))
                    elif one_site[round]<one_index:
                        Calculate.append((((one_index-one_site[round])**2+1)**0.5)*10 * 2**(5+key_round))
                    else:
                        Calculate.append((((one_index-one_site[round])**2+1)**0.5) * 2**(5+key_round))
                    
                    if r==0:
                        if round<len(one_site)-1:
                            round += 1
                        cal = one_index
                        if one_index < 5:
                            while j[one_index+1] == "1":
                                one_index += 1
                                if one_index == 5:
                                    break
                        Calculate.append(one_index-cal)
                key_round += 1
            a =0
            for s in Calculate:
                a+=s
            integer,floating = divmod(a,1)
            #將floating的小數點後分割成整數
            floating = str(floating)
            floating = floating.split(".")
            floating = floating[1]
            #將floating變為int
            cipher_text.append(int(integer))
            cipher_text.append(floating)
        cI = ""
        cI = "A".join(str(x) for x in cipher_text)
        return cI
    
    def decrypt(self,cipher_text,key):
        #將密文 "string,string,string,string" 轉換成list [int,int,int,int]
        ci = cipher_text.split("A")
        cipherText = []
        #將每兩個數字組成一個浮點數

        for i in range(0,int(len(ci)),2):
            cipherText.append(F"{ci[i]}.{ci[i+1]}")
            
        self.set_cipher_text(cipherText)
        decript_text = []
        #字母表由0~9,A~Z,a~z組成
        letter = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        #將二進制字母表map到key組成的密文
        cipher_letter = []
        cipher_letter = self.encrypt(letter,key)
        c = cipher_letter.split("A")
        cipherLetter = []
        for j in range(0,int(len(c)),2):
            cipherLetter.append(F"{c[j]}.{c[j+1]}")
  
        #將密文轉換成字母
        for L in self.get_cipher_text():
            for N in cipherLetter:   
                if L == N:
                    decript_text.append(letter[cipherLetter.index(N)])
        decript_text = "".join(decript_text)
        return decript_text
    


def main():
    #usage
    while True:
        key = input("Enter the key: ")
        plain_text = input("Enter the message: ")
        one = one_con()
        cipher_text = one.encrypt(plain_text,key)
        print(cipher_text)
        cipher_text = input("Press Enter to decrypt the message: ")
        plain_text = one.decrypt(cipher_text,key)
        print(plain_text)

if __name__ == "__main__":
    main()