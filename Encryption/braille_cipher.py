import string

braille_dict = {**dict.fromkeys(['a', 'A', '1'], '100000'), 
                **dict.fromkeys(['b', 'B', '2'], '110000'),
                **dict.fromkeys(['c', 'C', '3'], '100100'),
                **dict.fromkeys(['d', 'D', '4'], '100110'),
                **dict.fromkeys(['e', 'E', '5'], '100010'),
                **dict.fromkeys(['f', 'F', '6'], '110100'),
                **dict.fromkeys(['g', 'G', '7'], '110110'),
                **dict.fromkeys(['h', 'H', '8'], '110010'),
                **dict.fromkeys(['i', 'I', '9'], '010100'),
                **dict.fromkeys(['j', 'J', '0'], '010110'),
                **dict.fromkeys(['k', 'K'], '101000'),
                **dict.fromkeys(['l', 'L'], '111000'),
                **dict.fromkeys(['m', 'M'], '101100'),
                **dict.fromkeys(['n', 'N'], '101110'),
                **dict.fromkeys(['o', 'O'], '101010'),
                **dict.fromkeys(['p', 'P'], '111100'),
                **dict.fromkeys(['q', 'Q'], '111110'),
                **dict.fromkeys(['r', 'R'], '111010'),
                **dict.fromkeys(['s', 'S'], '011100'),
                **dict.fromkeys(['t', 'T'], '011110'),
                **dict.fromkeys(['u', 'U'], '101001'),
                **dict.fromkeys(['v', 'V'], '111001'),
                **dict.fromkeys(['w', 'W'], '010111'),
                **dict.fromkeys(['x', 'X'], '101101'),
                **dict.fromkeys(['y', 'Y'], '101111'),
                **dict.fromkeys(['z', 'Z'], '101011'),}

braille_extend_dict = {'BIG_START' : '000001',
                       'BIG_END1' : '000001',
                       'BIG_END2' : '001000',
                       'DIGIT_START' : '001111',
                       'DIGIT_END' : '000011',}

order_list = []
order_list.extend(string.ascii_lowercase[:26][i:i+1] for i in range(26))
order_list.extend(string.ascii_uppercase[:26][i:i+1] for i in range(26))
order_list.extend(string.digits[1:10][i:i+1] for i in range(9))
order_list.extend('0')

braille_rotate_dict = {}
cipher_dict = {}

def encode(plain_text, key):
    # plain_text = 'TEST'
    # key = 'Hello'
    
    print('Here is encode!')
    
    braille_rotate_dict = {}
    cipher_dict = {}
    
    #處理Key
    temp_key = list(key[j:j+1] for j in range(len(key)))
    braille_key = []
    continuous = []
    double_big_flag = False
    digit_flag = False
    reverse_flag = False
    
    #根據規則將key一一判斷前面是否要新增符號
    for i in range(len(temp_key)):
        if(i == len(temp_key) - 1):
            if(temp_key[i].isupper()):
                if(len(continuous) != 0):
                    continuous.extend([temp_key[i]])
                    braille_key.extend(continuous)
                    continuous = []
                    double_big_flag = False
                else:
                    braille_key.extend(['BIG_START', temp_key[i]])
                break
            elif(temp_key[i].islower()):
                braille_key.extend([temp_key[i]])
                break
            elif(temp_key[i].isdigit()):
                if(len(continuous) != 0):
                    continuous.extend([temp_key[i]])
                    braille_key.extend(continuous)
                    continuous = []
                    digit_flag = False
                else:
                    braille_key.extend(['DIGIT_START', temp_key[i]])
                break
            
        
        if(temp_key[i].isupper()):
            if((temp_key[i + 1].islower() or temp_key[i + 1].isdigit()) and len(continuous) == 0):
                braille_key.extend(['BIG_START',temp_key[i]])
            elif((temp_key[i + 1].islower() or temp_key[i + 1].isdigit()) and len(continuous) != 0):
                continuous.extend([temp_key[i], 'BIG_END1', 'BIG_END2'])
                braille_key.extend(continuous)
                continuous = []
                double_big_flag = False
            else:
                if(not double_big_flag):
                    braille_key.extend(['BIG_START', 'BIG_START'])
                    double_big_flag = True
                continuous.extend([temp_key[i]])
        elif(temp_key[i].islower()):
            braille_key.extend([temp_key[i]])
        elif(temp_key[i].isdigit()):
            if((temp_key[i + 1].islower() or temp_key[i + 1].isupper()) and len(continuous) == 0):
                braille_key.extend(['DIGIT_START',temp_key[i],'DIGIT_END'])
            elif((temp_key[i + 1].islower() or temp_key[i + 1].isupper()) and len(continuous) != 0):
                continuous.extend([temp_key[i],'DIGIT_END'])
                braille_key.extend(continuous)
                continuous = []
                digit_flag = False
            else:
                if(not digit_flag):
                    braille_key.extend(['DIGIT_START'])
                    digit_flag = True
                continuous.extend([temp_key[i]])
                

    #將擴充完的key轉為二進制
    binary_braille_key = []
    for key_char in braille_key:
        if(len(key_char) > 1):
            binary_braille_key.extend([braille_extend_dict[key_char]])
        else:
            binary_braille_key.extend([braille_dict[key_char]])
    
    #對每位key進行XOR運算
    key_result = int(binary_braille_key[0], 2)
    for i in range(len(binary_braille_key) - 1):
        key_result = key_result ^ int(binary_braille_key[i + 1], 2)
        
    #判斷出來的值為奇數或偶數，reverse_flag為True時，比大
    if(key_result % 2 == 1):
        reverse_flag = True
    else:
        reverse_flag = False
        
    
    #根據key長度將盲文進行旋轉，套入特殊規則後並轉換為10進位存入braille_rotate_list   
    for dict_key in braille_dict.keys():  
        if(dict_key.islower()):
            temp_tuple = ('1', '0')
        elif(dict_key.isupper()):
            temp_tuple = ('0', '1')
        elif(dict_key.isdigit()):
            temp_tuple = ('0', '0')
            
        value_tuple = temp_tuple + tuple(braille_dict[dict_key][j:j+1] for j in range(6)) 
    
        for i in range(key_result % 6):
            temp_tuple = ()
            temp_tuple = temp_tuple + (value_tuple[0],)
            temp_tuple = temp_tuple + (value_tuple[1],)
            temp_tuple = temp_tuple + (value_tuple[3],)
            temp_tuple = temp_tuple + (value_tuple[4],)
            temp_tuple = temp_tuple + (value_tuple[7],)
            temp_tuple = temp_tuple + (value_tuple[2],)
            temp_tuple = temp_tuple + (value_tuple[5],)
            temp_tuple = temp_tuple + (value_tuple[6],)
 
            value_tuple = temp_tuple

        rotated_binary = ''.join(value_tuple)
        braille_rotate_dict.update({dict_key : int(rotated_binary, 2)}) #存進去的時候就已轉為十進位
    
    #根據key算出來為奇數或偶數，將剛剛算出來數字進行升序或降序排序
    sorted_dict = dict(sorted(braille_rotate_dict.items(), key=lambda x: x[1], reverse = reverse_flag))
    
    
    # print(sorted_dict)
    #排序完後，根據order_list指定的順序將其存放回cipher_dict中
    for order_key, (cipher_key, _) in zip(order_list, sorted_dict.items()):
        cipher_dict.update({order_key : cipher_key})

    # print(cipher_dict)

    plain_text = list(plain_text[j:j+1] for j in range(len(plain_text)))
    
    cipher_text = []
    for text in plain_text:
        cipher_text.extend(cipher_dict[text])
    
    plain_text = ''.join(plain_text)
    cipher_text = ''.join(cipher_text)

    # print(f'明文 : {plain_text} ; Key: {key} ; 密文 : {cipher_text}')
    
    return cipher_text
    
def decode(cipher_text, key):
    print('Here is decode!')
    
    braille_rotate_dict = {}
    cipher_dict = {}
    
    #處理Key
    temp_key = list(key[j:j+1] for j in range(len(key)))
    braille_key = []
    continuous = []
    double_big_flag = False
    digit_flag = False
    reverse_flag = False
    
    #根據規則將key一一判斷前面是否要新增符號
    for i in range(len(temp_key)):
        if(i == len(temp_key) - 1):
            if(temp_key[i].isupper()):
                if(len(continuous) != 0):
                    continuous.extend([temp_key[i]])
                    braille_key.extend(continuous)
                    continuous = []
                    double_big_flag = False
                else:
                    braille_key.extend(['BIG_START', temp_key[i]])
                break
            elif(temp_key[i].islower()):
                braille_key.extend([temp_key[i]])
                break
            elif(temp_key[i].isdigit()):
                if(len(continuous) != 0):
                    continuous.extend([temp_key[i]])
                    braille_key.extend(continuous)
                    continuous = []
                    digit_flag = False
                else:
                    braille_key.extend(['DIGIT_START', temp_key[i]])
                break
            
        
        if(temp_key[i].isupper()):
            if((temp_key[i + 1].islower() or temp_key[i + 1].isdigit()) and len(continuous) == 0):
                braille_key.extend(['BIG_START',temp_key[i]])
            elif((temp_key[i + 1].islower() or temp_key[i + 1].isdigit()) and len(continuous) != 0):
                continuous.extend([temp_key[i], 'BIG_END1', 'BIG_END2'])
                braille_key.extend(continuous)
                continuous = []
                double_big_flag = False
            else:
                if(not double_big_flag):
                    braille_key.extend(['BIG_START', 'BIG_START'])
                    double_big_flag = True
                continuous.extend([temp_key[i]])
        elif(temp_key[i].islower()):
            braille_key.extend([temp_key[i]])
        elif(temp_key[i].isdigit()):
            if((temp_key[i + 1].islower() or temp_key[i + 1].isupper()) and len(continuous) == 0):
                braille_key.extend(['DIGIT_START',temp_key[i],'DIGIT_END'])
            elif((temp_key[i + 1].islower() or temp_key[i + 1].isupper()) and len(continuous) != 0):
                continuous.extend([temp_key[i],'DIGIT_END'])
                braille_key.extend(continuous)
                continuous = []
                digit_flag = False
            else:
                if(not digit_flag):
                    braille_key.extend(['DIGIT_START'])
                    digit_flag = True
                continuous.extend([temp_key[i]])
                

    #將擴充完的key轉為二進制
    binary_braille_key = []
    for key_char in braille_key:
        if(len(key_char) > 1):
            binary_braille_key.extend([braille_extend_dict[key_char]])
        else:
            binary_braille_key.extend([braille_dict[key_char]])
    
    #對每位key進行XOR運算
    key_result = int(binary_braille_key[0], 2)
    for i in range(len(binary_braille_key) - 1):
        key_result = key_result ^ int(binary_braille_key[i + 1], 2)
        
    #判斷出來的值為奇數或偶數，reverse_flag為True時，比大
    if(key_result % 2 == 1):
        reverse_flag = True
    else:
        reverse_flag = False
        
    
    #根據key長度將盲文進行旋轉，套入特殊規則後並轉換為10進位存入braille_rotate_list   
    for dict_key in braille_dict.keys():  
        if(dict_key.islower()):
            temp_tuple = ('1', '0')
        elif(dict_key.isupper()):
            temp_tuple = ('0', '1')
        elif(dict_key.isdigit()):
            temp_tuple = ('0', '0')
            
        value_tuple = temp_tuple + tuple(braille_dict[dict_key][j:j+1] for j in range(6)) 
    
        for i in range(key_result % 6):
            temp_tuple = ()
            temp_tuple = temp_tuple + (value_tuple[0],)
            temp_tuple = temp_tuple + (value_tuple[1],)
            temp_tuple = temp_tuple + (value_tuple[3],)
            temp_tuple = temp_tuple + (value_tuple[4],)
            temp_tuple = temp_tuple + (value_tuple[7],)
            temp_tuple = temp_tuple + (value_tuple[2],)
            temp_tuple = temp_tuple + (value_tuple[5],)
            temp_tuple = temp_tuple + (value_tuple[6],)
 
            value_tuple = temp_tuple

        rotated_binary = ''.join(value_tuple)
        braille_rotate_dict.update({dict_key : int(rotated_binary, 2)}) #存進去的時候就已轉為十進位
    
    #根據key算出來為奇數或偶數，將剛剛算出來數字進行升序或降序排序
    sorted_dict = dict(sorted(braille_rotate_dict.items(), key=lambda x: x[1], reverse = reverse_flag))
    
    
    #排序完後，根據order_list指定的順序將其存放回cipher_dict中
    for order_key, (cipher_key, _) in zip(order_list, sorted_dict.items()):
        cipher_dict.update({cipher_key : order_key})

    # print(cipher_dict)

    cipher_text = list(cipher_text[j:j+1] for j in range(len(cipher_text)))
    
    plain_text = []
    for text in cipher_text:
        plain_text.extend(cipher_dict[text])
    
    plain_text = ''.join(plain_text)
    cipher_text = ''.join(cipher_text)

    # print(f'明文 : {plain_text} ; Key: {key} ; 密文 : {cipher_text}')
    
    return cipher_text