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
            floating = int(floating)
            d=(int(integer),floating)
            cipher_text.append(d)
        return cipher_text
    
    def decrypt(self,cipher_text,key):
        self.set_cipher_text(cipher_text)
        decript_text = []
        #字母表由0~9,A~Z,a~z組成
        letter = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        #將二進制字母表map到key組成的密文
        cipher_letter = []
        self.set_plain_text(letter)
        cipher_letter = self.encrypt(key,letter)
        #將密文轉換成字母
        for i in self.get_cipher_text():
            for j in cipher_letter:   
                if i == j:
                    decript_text.append(letter[cipher_letter.index(j)])
        return decript_text
    


def main():
    #usage
    while True:
        key = input("Enter the key: ")
        plain_text = input("Enter the message: ")
        one = one_con()
        cipher_text = one.encrypt(key,plain_text)
        print(cipher_text)
        plain_text = one.decrypt(key,cipher_text)
        print(plain_text)

if __name__ == "__main__":
    main()
                    
            

        
