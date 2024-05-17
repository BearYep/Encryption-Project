def fold_and_encrypt(plain_text,key):
    # 第一次對折
    plain_text = plain_text.replace(" ", "")
    new_key = ""
    even_key = True
    if key[-1].isdigit():
        new_key = key[-1]
        mid_reform_index = int(new_key) % len(plain_text)
        if int(new_key) % 2 != 0:
            even_key = False
    else:    
        for i in range(len(key)):
            new_key += str(ord(key[i]))
        #string_key = str(new_key)
        print(int(new_key[-1]))
        mid_reform_index = int(new_key[-1]) % len(plain_text)
        if int(new_key[-1]) % 2 != 0:
            even_key = False

    print("mid_reform_index:", mid_reform_index)
    if len(plain_text) <= 4:
        if len(plain_text) % 2 != 0:
            threefirst_half = plain_text[:1]
            print(threefirst_half)
            threesecond_half = plain_text[2:]
            print(threesecond_half)
            threemid_word = plain_text[1]
            print(threemid_word)
            if not even_key:
                reform_one = threesecond_half + threefirst_half
            else:
                reform_one = threefirst_half + threesecond_half                
            print(mid_reform_index)        
            reform_one = reform_one[:mid_reform_index] + threemid_word + reform_one[mid_reform_index:]
            return reform_one
        else:   #post -> tpso
            four_half = len(plain_text) // 2
            fourfirst_half = plain_text[:four_half]
            foursecond_half = plain_text[four_half:]
            four_half_half = len(fourfirst_half) // 2
            fourfirst_half_folded1 = fourfirst_half[:four_half_half]
            print(fourfirst_half_folded1)
            fourfirst_half_folded2 = fourfirst_half[four_half_half:]
            fourfirst_half_folded2reverse = fourfirst_half_folded2[::-1]
            print(fourfirst_half_folded2reverse)
            foursecond_half_folded1 = foursecond_half[:four_half_half]
            print(foursecond_half_folded1)
            foursecond_half_folded2 = foursecond_half[four_half_half:]
            foursecond_half_folded2reverse = foursecond_half_folded2[::-1]
            print(foursecond_half_folded2reverse)
            if not even_key:
                reform = foursecond_half_folded2reverse + fourfirst_half_folded1 + foursecond_half_folded1 +fourfirst_half_folded2reverse
            else:
                reform = fourfirst_half_folded2reverse + foursecond_half_folded1 + fourfirst_half_folded1 + foursecond_half_folded2reverse
            return reform
             
    if len(plain_text) % 2 != 0:
        half_length = len(plain_text) // 2
        first_half = plain_text[:half_length]
        print(first_half)
        second_half = plain_text[half_length + 1:]
        print(second_half)
        
        # 兩段文字第二次對折
        half_half_length = len(first_half) // 2
        first_half_folded1 = first_half[:half_half_length]
        print(first_half_folded1)
        first_half_folded2 = first_half[half_half_length:]
        first_half_folded2reverse = first_half_folded2[::-1]
        print(first_half_folded2reverse)
        second_half_folded1 = second_half[:half_half_length]
        print(second_half_folded1)
        second_half_folded2 = second_half[half_half_length:]
        second_half_folded2reverse = second_half_folded2[::-1]
        print(second_half_folded2reverse)
        
        # 合併兩段文字提出來
        cipher_text = ''
        #column first
        for i in range(int(len(plain_text) / 4) + 1):
            if i < len(second_half_folded2reverse):
                cipher_text += second_half_folded2reverse[i]
            if i < len(first_half_folded1):
                cipher_text += first_half_folded1[i]
            if i < len(second_half_folded1):
                cipher_text += second_half_folded1[i]
            if i < len(first_half_folded2):
                cipher_text += first_half_folded2reverse[i]
    
        devided_cipher_text = [cipher_text[i:i+4] for i in range(0, len(cipher_text), 4)]
        new_cipher_text = ''
        if even_key:
            for i in range(len(devided_cipher_text)):
                if i % 2 == 0:
                    new_cipher_text += devided_cipher_text[i][::-1]
                else:
                    new_cipher_text += devided_cipher_text[i]
        else:
            for i in range(len(devided_cipher_text)):
                if i % 2 != 0:
                    new_cipher_text += devided_cipher_text[i][::-1]
                else:
                    new_cipher_text += devided_cipher_text[i]
        print(mid_reform_index)            
        new_cipher_text = new_cipher_text[:mid_reform_index] + plain_text[half_length] + new_cipher_text[mid_reform_index:]                                
        return new_cipher_text

    elif len(plain_text) % 2 == 0:
        half_length = len(plain_text) // 2
        first_half = plain_text[:half_length]
        print(first_half)
        second_half = plain_text[half_length:]
        print(second_half)
        
        # 兩段文字第二次對折
        half_half_length = len(first_half) // 2
        first_half_folded1 = first_half[:half_half_length]
        print(first_half_folded1)
        first_half_folded2 = first_half[half_half_length:]
        first_half_folded2reverse = first_half_folded2[::-1]
        print(first_half_folded2reverse)
        second_half_folded1 = second_half[:half_half_length]
        print(second_half_folded1)
        second_half_folded2 = second_half[half_half_length:]
        second_half_folded2reverse = second_half_folded2[::-1]
        print(second_half_folded2reverse)
        
        # 合併兩段文字提出來
        cipher_text = ''
        #column first
        for i in range(int(len(plain_text) / 4) + 1):
            if i < len(second_half_folded2reverse):
                cipher_text += second_half_folded2reverse[i]
            if i < len(first_half_folded1):
                cipher_text += first_half_folded1[i]
            if i < len(second_half_folded1):
                cipher_text += second_half_folded1[i]
            if i < len(first_half_folded2):
                cipher_text += first_half_folded2reverse[i]
    
        devided_cipher_text = [cipher_text[i:i+4] for i in range(0, len(cipher_text), 4)]
        new_cipher_text = ''
        if even_key:
            for i in range(len(devided_cipher_text)):
                if i % 2 == 0:
                    new_cipher_text += devided_cipher_text[i][::-1]
                else:
                    new_cipher_text += devided_cipher_text[i]
        else:
            for i in range(len(devided_cipher_text)):
                if i % 2 != 0:
                    new_cipher_text += devided_cipher_text[i][::-1]
                else:
                    new_cipher_text += devided_cipher_text[i]
        print(mid_reform_index) 
        cipher_text = new_cipher_text
        return cipher_text           


def decrypt_and_unfold(cipher_text,key):
    new_key = ""
    even_key = True
    if key[-1].isdigit():
        new_key = key[-1]
        mid_reform_index = int(new_key) % len(cipher_text)
        if int(new_key) % 2 != 0:
            even_key = False
    else:    
        for i in range(len(key)):
            new_key += str(ord(key[i]))
        #string_key = str(new_key)
        print(int(new_key[-1]))
        mid_reform_index = int(new_key[-1]) % len(cipher_text)
        if int(new_key[-1]) % 2 != 0:
            even_key = False
    if len(cipher_text) % 2 != 0:
        #if ((len(cipher_text) - 1) / 2) % 2 != 0:    
            print("yes: ", mid_reform_index)
            without_midword_cipher_text = cipher_text[:mid_reform_index] + cipher_text[mid_reform_index+1:]
            
            new_without_midword_cipher_text = without_midword_cipher_text[:len(without_midword_cipher_text) - len(without_midword_cipher_text) % 4]
            print(new_without_midword_cipher_text)
            arrays = [[],[],[],[]]
            count = 0
            for i in range(0,len(new_without_midword_cipher_text),4):
                if count % 2 == 0:
                    arrays[3].append(new_without_midword_cipher_text[i])
                    arrays[0].append(new_without_midword_cipher_text[i+1])
                    arrays[2].append(new_without_midword_cipher_text[i+2])
                    arrays[1].append(new_without_midword_cipher_text[i+3])
                    count += 1
                else:
                    arrays[1].append(new_without_midword_cipher_text[i])
                    arrays[2].append(new_without_midword_cipher_text[i+1])
                    arrays[0].append(new_without_midword_cipher_text[i+2])
                    arrays[3].append(new_without_midword_cipher_text[i+3])
                    count += 1
            if count % 2 != 0 and len(without_midword_cipher_text) % 4 != 0:
                arrays[1].append(without_midword_cipher_text[-2])
                arrays[3].append(without_midword_cipher_text[-1])
            elif count % 2 == 0 and len(without_midword_cipher_text) % 4 != 0:
                arrays[3].append(without_midword_cipher_text[-2])
                arrays[1].append(without_midword_cipher_text[-1])                
            print(arrays)    
            arrays[1].reverse()
            arrays[3].reverse()
            if even_key:
                plain_text = ''.join(arrays[2] + arrays[3] + arrays[0] + arrays[1])
            else:    
                plain_text = ''.join(arrays[0] + arrays[1] + arrays[2] + arrays[3])
            plain_text = plain_text[:len(cipher_text) // 2] + cipher_text[mid_reform_index] + plain_text[len(cipher_text) // 2 :]
            #plain_text = str(plain_text[:len(cipher_text)//2]) + str(plain_text[len(plain_text)//2+1]) + str(plain_text[len(cipher_text)//2:])
            print("plain_text = ",str(plain_text))
            return str(plain_text)
    
    else:
        new_cipher_text = cipher_text[:len(cipher_text) - len(cipher_text) % 4]
        print(new_cipher_text)
        arrays = [[],[],[],[]]
        count = 0
        for i in range(0,len(new_cipher_text),4):
            if count % 2 == 0:
                arrays[3].append(new_cipher_text[i])
                arrays[0].append(new_cipher_text[i+1])
                arrays[2].append(new_cipher_text[i+2])
                arrays[1].append(new_cipher_text[i+3])
                count += 1
            else:
                arrays[1].append(new_cipher_text[i])
                arrays[2].append(new_cipher_text[i+1])
                arrays[0].append(new_cipher_text[i+2])
                arrays[3].append(new_cipher_text[i+3])
                count += 1
        if count % 2 != 0 and len(cipher_text) % 4 != 0:
            arrays[1].append(cipher_text[-2])
            arrays[3].append(cipher_text[-1])
        elif count % 2 == 0 and len(cipher_text) % 4 != 0:
            arrays[3].append(cipher_text[-2])
            arrays[1].append(cipher_text[-1])                
        print(arrays)    
        arrays[1].reverse()
        arrays[3].reverse()
        if even_key:
            plain_text = ''.join(arrays[2] + arrays[3] + arrays[0] + arrays[1])
        if not even_key and len(cipher_text) <= 4:
            plain_text = ''.join(arrays[0] + arrays[1] + arrays[2] + arrays[3])    
        if len(cipher_text) <= 4 and even_key:
            plain_text = ''.join(arrays[0] + arrays[1] + arrays[2] + arrays[3])
        else:    
            plain_text = ''.join(arrays[0] + arrays[1] + arrays[2] + arrays[3])

        if even_key and len(cipher_text) <= 4:
            plain_text = plain_text[len(cipher_text) // 2:] + plain_text[:len(cipher_text) // 2]
            print("Even key, <= 4")
        elif not even_key and len(cipher_text) <= 4:
            plain_text = plain_text[:len(cipher_text) // 2] + plain_text[len(cipher_text) // 2:]
        elif even_key and len(cipher_text) > 4:
            plain_text = plain_text[len(cipher_text) // 2:] + plain_text[:len(cipher_text) // 2]
            print("Even key, > 4")    
        else:
            #plain_text = plain_text[:len(cipher_text) // 2] + plain_text[len(cipher_text) // 2:]
            print("plain_text = ",str(plain_text))
            return plain_text      
        #plain_text = str(plain_text[:len(cipher_text)//2]) + str(plain_text[len(plain_text)//2+1]) + str(plain_text[len(cipher_text)//2:])
        print("plain_text = ",str(plain_text))
        return str(plain_text)

                

#test!!!
plain_text = "hall"
key = "5abc"
#secret_text = "I!U!LOSHOYOCVEMU"
cipher_text = fold_and_encrypt(plain_text,key)
print("加密後的密文：", cipher_text)
decrypted_text = decrypt_and_unfold(cipher_text,key)
#plain_text = plain_text.replace("!", "")
#print("解密明文：", plain_text)
