
def create_array_from_plain(input_string):
    
    characters = list(input_string)
    redundant = ""
    # 計算需要的列數
    if(len(characters) % 2 == 1):
        redundant = characters[-1]
        characters.pop()
        num_rows = int(len(characters) / 2)
    else:
        num_rows = int(len(characters) / 2)
    
    # 初始化二維陣列
    array = [[None for _ in range(2)] for _ in range(num_rows)]
    
    row_count = 0
    for i in range(0, len(characters), 2):
        array[row_count][0] = characters[i]
        if i + 1 < len(characters) and characters[i + 1] is not None: #檢查合法
            array[row_count][1] = characters[i + 1]
        row_count += 1

    return array, redundant

def encode(plain_text, key):
    if(len(plain_text) == 1):
        return plain_text
    
    keynum_array = [letter_to_number(char) for char in key]
    array, redundant = create_array_from_plain(plain_text)

    for keynum in keynum_array:
        for row_count in range(0, len(array) - 1):
            if(keynum % 2 == 0):
                temp = array[row_count][1] 
                array[row_count][1] = array[row_count][0]
                array[row_count][0] = array[row_count + 1][0]
                array[row_count + 1][0] = array[row_count + 1][1]
                array[row_count + 1][1] = temp
            else:
                temp = array[row_count][1] 
                array[row_count][1] = array[row_count + 1][1]
                array[row_count + 1][1] = array[row_count + 1][0]
                array[row_count + 1][0] = array[row_count][0]
                array[row_count][0] = temp  

    result_string = ""
    for i in range(0, len(array)):
        if array[i][0] is not None:
            result_string += array[i][0]
    for i in range(0, len(array)):
        if array[i][1] is not None:
            result_string += array[i][1]


    offset = len(keynum_array) % len(result_string)
    before = result_string[:len(result_string) - offset]
    after = result_string[len(result_string) - offset:]
    result_string = before[::-1] + after[::-1]
    result_string = result_string[::-1]


    result_string = result_string + redundant


    return result_string

def create_array_from_cipher(input_string):
    
    characters = list(input_string)
    
    # 計算需要的列數
    num_rows = int(len(characters) / 2)
    
    # 初始化二維陣列
    array = [[None for _ in range(2)] for _ in range(num_rows)]
    
    row_count = 0
    for i in range(0, int(len(characters) / 2)):
        array[row_count][0] = characters[i]
        if i + int(len(characters) / 2) < len(characters) and characters[i + int(len(characters) / 2)] is not None: #檢查合法
            array[row_count][1] = characters[i + int(len(characters) / 2)]
        row_count += 1

    return array

def decode(cipher_text, key):  
    if(len(cipher_text) == 1):
        return cipher_text
    
    keynum_array = [letter_to_number(char) for char in key]
    redundant = ""


    if(len(cipher_text) % 2 == 1):
        redundant = cipher_text[-1]
        cipher_text = cipher_text[:-1]
    
    offset = len(keynum_array) % len(cipher_text)
    before = cipher_text[:offset]
    after = cipher_text[offset:]
    cipher_text = before[::-1] + after[::-1]
    cipher_text = cipher_text[::-1]

    array = create_array_from_cipher(cipher_text)


    for keynum in reversed(keynum_array):
        for row_count in range(len(array) - 2, -1, -1):
            if(keynum % 2 == 0):
                temp = array[row_count][1] 
                array[row_count][1] = array[row_count + 1][1]
                array[row_count + 1][1] = array[row_count + 1][0]
                array[row_count + 1][0] = array[row_count][0]
                array[row_count][0] = temp  
            else:
                temp = array[row_count][1] 
                array[row_count][1] = array[row_count][0]
                array[row_count][0] = array[row_count + 1][0]
                array[row_count + 1][0] = array[row_count + 1][1]
                array[row_count + 1][1] = temp

    result_string = ""
    for i in range(0, len(array)):
        if array[i][0] is not None:
            result_string += array[i][0]
        if array[i][1] is not None:
            result_string += array[i][1]

    if(redundant != ""):
        result_string = result_string + redundant

    return result_string

def letter_to_number(letter):
    if(letter.isdigit()):
        return int(letter)
    else:
        return ord(letter.lower()) - 96 if letter.isalpha() else None