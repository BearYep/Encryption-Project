import random

class FibraEncryption:
    def __init__(self):
        pass

    def char_to_number(self, char): # 文字轉數字代號
        num  = ord(char)
        if (num >= 48 and num <= 57):
            return ord(char) - ord('0') # 0為0
        elif (num >= 65 and num <= 90):
            return ord(char) - ord('A') + 10 # A為10
        elif (num >= 97 and num <= 122):
            return ord(char) - ord('a') + 36 # a為36
        
    def number_to_char(self, num): # 數字代號轉文字
        if (0 <= num <= 9): 
            return chr(num + ord('0')) # 0為0
        elif (10 <= num <= 35):
            return chr(num + ord('A') - 10) # 10為A
        elif (36 <= num <= 61):
            return chr(num + ord('a') - 36) # 36為a

    def text_to_numbers(self, text):  # 文字轉數字列表
        list = []
        for char in text:
            list.append(self.char_to_number(char))
        return list

    def get_factors(self, n): # 找因數
        factors = []
        for i in range(1, n + 1):
            if n % i == 0:
                factors.append(i)
        return factors 

    def text_to_matrix(self, text, num_rows, num_cols): # 建立矩陣
        numbers = self.text_to_numbers(text)  
        matrix = [[0] * num_cols for _ in range(num_rows)]  # 建立以0填充的矩陣
        
        index = 0
        for i in range(num_rows):
            for j in range(num_cols):
                if index < len(numbers):
                    matrix[i][j] = numbers[index]
                    index += 1
        return matrix

    def enlarge_matrix(self, matrix, original_rows, original_cols):

        # 新矩陣的行數和列數
        new_rows = original_rows
        new_cols = original_cols * 4

        # 複製矩陣四次
        enlarged_matrix= []
        for i in range(new_rows):
            row = []
            for j in range(new_cols):
                if i < original_rows and j < original_cols:  # 保留原始明文的部分
                    row.append(matrix[i][j])
                else:
                    row.append(random.randint(0, 61))  # 填充部分隨機生成數字
            enlarged_matrix.append(row)

        return enlarged_matrix

    # 還原原始的密文矩陣大小
    def shrink_matrix(self, enlarged_matrix, original_rows, original_cols):
        # 縮小為原始大小
        original_matrix = [enlarged_matrix[i][:original_cols] for i in range(original_rows)]
        return original_matrix

    def matrix_A(self, matrix): # 轉置
        return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

    def matrix_B(self, matrix): # 水平鏡射
        return [[matrix[i][len(matrix[0])-1-j] for j in range(len(matrix[0]))] for i in range(len(matrix))]

    def matrix_C(self, matrix):  # 每rows向右循環 仿AES
        num_rows = len(matrix)
        for i in range(num_rows):
            shift = i  # 根據行號計算位移量
            matrix[i] = matrix[i][-shift:] + matrix[i][:-shift]
        return matrix

    def invert_matrix_C(self, matrix):  # 反向行位移(rows) 仿AES
        num_rows = len(matrix)
        for i in range(num_rows):
            shift = i  # 根據行號計算位移量
            matrix[i] = matrix[i][shift:] + matrix[i][:shift]
        return matrix

    def matrix_D(self, matrix):  # 每cols向下循環 仿AES
        num_cols = len(matrix[0])
        for i in range(num_cols):
            shift = i
            matrix = [row[-shift:] + row[:-shift] for row in matrix]
        return matrix

    def invert_matrix_D(self, matrix):  # 反向列位移(cols) 仿AES
        num_cols = len(matrix[0])
        for i in range(num_cols):
            shift = i
            matrix = [row[-shift:] + row[:-shift] for row in matrix]
        return matrix

    def encrypt(self, plaintext, key):
        key = self.generate_child_key(key)
        all_factors = self.get_factors(len(plaintext))
        num_factors = len(all_factors)
        if num_factors % 2 == 1:  # 奇數個因數
            num_rows = num_cols = all_factors[num_factors // 2]
        else:  # 偶數個因數
            middle_index = num_factors // 2
            num_rows = all_factors[middle_index]
            num_cols = all_factors[middle_index - 1]
   
        cipher_matrix = self.text_to_matrix(plaintext, num_rows, num_cols) # 文字轉矩陣
        cipher_matrix = self.enlarge_matrix(cipher_matrix, num_rows, num_cols) # 放大矩陣

        key_list = self.text_to_numbers(key)
        
        for i in range(len(key_list)):
            if key_list[i] % 2 == 1: # 奇數轉置
                cipher_matrix = self.matrix_A(cipher_matrix)
                cipher_matrix = self.matrix_C(cipher_matrix) # 每rows向右循環
            else: # 偶數水平鏡射
                cipher_matrix = self.matrix_B(cipher_matrix)
                cipher_matrix = self.matrix_D(cipher_matrix) # 每cols向下循環

        # 將加密後的矩陣轉換回加密後的文字
        cipher_text =''
        for row in cipher_matrix:
            for num in row:
                cipher_text += self.number_to_char(num)
        return cipher_text

    def decrypt(self, ciphertext, key):
        key = self.generate_child_key(key)
        key_list = self.text_to_numbers(key)
        all_factors = self.get_factors(int(len(ciphertext)/4)) # 加密矩陣長度原為長度4倍 除四找原大小
        num_factors = len(all_factors)

        if num_factors % 2 == 1:  # 奇數個因數
            new_rows = new_cols = all_factors[num_factors // 2] *2
        else:  # 偶數個因數
            middle_index = num_factors // 2
            original_rows = all_factors[middle_index]
            original_cols = all_factors[middle_index - 1]
            new_rows = original_rows # 加密矩陣cols為原矩陣的四倍
            new_cols = original_cols *4 # 加密矩陣cols為原矩陣的四倍

        for i in range(len(key_list)): # 查看加密時rows cols的變化
            if key_list[i] % 2 == 1: # 奇數轉置rows cols互換
                new_rows, new_cols = new_cols, new_rows
            else: # 偶數水平鏡射 不變
                pass

        cipher_matrix = self.text_to_matrix(ciphertext, new_rows, new_cols)
        
        # 反向遍歷key列表，先進行奇數或偶數的處理
        for i in reversed(range(len(key_list))):
            if key_list[i] % 2 == 1: # 奇數轉置 
                cipher_matrix = self.invert_matrix_C(cipher_matrix) # 反向rows循環
                cipher_matrix = self.matrix_A(cipher_matrix)
            else: # 偶數水平鏡射 
                cipher_matrix = self.invert_matrix_D(cipher_matrix) # 反向cols循環
                cipher_matrix = self.matrix_B(cipher_matrix)

        cipher_matrix = self.shrink_matrix(cipher_matrix, original_rows, original_cols) # 還原正常大小

        # 將解密後的矩陣轉換回原始明文
        decrypted_text = ''
        for row in cipher_matrix:
            for num in row:
                decrypted_text += self.number_to_char(num)
        
        return decrypted_text

    # 第一位位移1 第二位位移2 第三位位移3  第四位位移4 第五位位移5 以此往復生成子key
    def generate_child_key(self, original_key):
        key_list = self.text_to_numbers(original_key)
        cycles = sum(key_list) - 150
        if cycles<5: cycles=5

        child_key = original_key
        current_key = original_key

        for _ in range(cycles):
            shifted_key = ''
            for i in range(len(current_key)):
                shifted_char = chr(((ord(current_key[i]) - ord('a') + i + 1) % 26) + ord('a'))
                shifted_key += shifted_char
            child_key += shifted_key
            current_key = shifted_key

        return child_key
    
    def main(self):
        # key = input("key:")
        # print("key:", key)

        # key = self.generate_child_key(key)
        # print(key)

        # PlainText = input("plaintext:")

        # CipherText = self.encrypt(PlainText, key)
        # print("cipher:", CipherText)

        # PlainText = self.decrypt(CipherText, key)
        # print("decrypted plaintext:", PlainText)
        self.test()
    
    def test(self, num_tests=100): # test
        count = 0
        flag = 1
        for _ in range(num_tests):
            count += 1
            cipher_text =''
            decrypted_text =''
            key = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))
            key = self.generate_child_key(key)
            # print(key)
            length = 5
            plaintext = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=length))
            # Encrypt
            cipher_text = self.encrypt(plaintext, key)

            # Decrypt
            decrypted_text = self.decrypt(cipher_text, key)

            # Check if decryption result matches plaintext
            if decrypted_text != plaintext:
                # print("Decryption error!")
                # print("Key:", key)
                # print("Plaintext:", plaintext)
                # print("Cipher text:", cipher_text)
                # print("Decrypted_text:", decrypted_text)
                # print(count)
                # print("------------------------")
                flag=0

            if count in (30, 50, 80, 100) and (flag == 1):
                # print("Key:", key)
                # print("Plaintext:", plaintext)
                # print("Cipher text:", cipher_text)
                # print("Decrypted_text:", decrypted_text)
                # print(count)
                # print("------------------------")
                pass

        if flag==1:
            # print("Success")
            pass

if __name__ == "__main__":
    pass
    # FibraEncryption = FibraEncryption()
    # FibraEncryption.main()