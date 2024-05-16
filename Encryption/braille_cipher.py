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

order_list = []
order_list.extend(string.ascii_lowercase[:26][i:i+1] for i in range(26))
order_list.extend(string.ascii_uppercase[:26][i:i+1] for i in range(26))
order_list.extend(string.digits[1:10][i:i+1] for i in range(9))
order_list.extend('0')

braille_rotate_dict = {}
cipher_dict = {}

def encode(plain_text, key):
    plain_text = 'TEST'
    key = 'HeLLO2024tesTTT'
    
    key_length = len(key)
    print('Here is encode!')
    #處理Key
    key = list(key[j:j+1] for j in range(len(key)))
    print(key)
    
    temp_key = []
    for i in range(key_length):
        if(key[i].islower()):
            temp_key.extend('a')
        elif(key[i].isupper()):
            temp_key.extend('A')
        elif(key[i].isdigit()):
            temp_key.extend('1')
    
    braille_key = []
    continuous_upper = []
    double_big_flag = False
    for i in range(len(temp_key)):
        if(i == len(temp_key) - 1):
            braille_key.extend(['A'])
            braille_key.extend(continuous_upper)
            break
        
        
        if(temp_key[i] == 'A'):
            if(temp_key[i + 1] != 'A' and len(continuous_upper) == 0):
                braille_key.extend(['BIG'])
                braille_key.extend('A')
            elif(temp_key[i + 1] != 'A' and len(continuous_upper) != 0):
                braille_key.extend(continuous_upper)
                braille_key.extend(['A', 'END'])
                continuous_upper = []
                double_big_flag = False
            else:
                if(not double_big_flag):
                    braille_key.extend(['BIG', 'BIG'])
                    double_big_flag = True
                continuous_upper.extend('A')
                
    
    print(braille_key)
    print(temp_key)
    #根據key長度將盲文進行旋轉，套入特殊規則後並轉換為10進位存入braille_rotate_list   
    for dict_key in braille_dict.keys():  
        if(dict_key.islower()):
            temp_tuple = ('1', '0')
        elif(dict_key.isupper()):
            temp_tuple = ('0', '1')
        elif(dict_key.isdigit()):
            temp_tuple = ('0', '0')
            
        value_tuple = temp_tuple + tuple(braille_dict[dict_key][j:j+1] for j in range(6)) 
    
        for i in range(key_length % 6):
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
    sorted_dict = dict(sorted(braille_rotate_dict.items(), key=lambda x: x[1], reverse=False))
    
    #排序完後，根據order_list指定的順序將其存放回cipher_dict中
    for order_key, (cipher_key, _) in zip(order_list, sorted_dict.items()):
        cipher_dict.update({order_key : cipher_key})

    print(cipher_dict)

    plain_text = list(plain_text[j:j+1] for j in range(len(plain_text)))
    
    cipher_text = []
    for text in plain_text:
        cipher_text.extend(cipher_dict[text])
    
    plain_text = ''.join(plain_text)
    cipher_text = ''.join(cipher_text)

    print(f'明文 : {plain_text} ; 密文 : {cipher_text}')
    
    return cipher_text
    
def decode(cipher_text, key):
    print('Here is decode!')