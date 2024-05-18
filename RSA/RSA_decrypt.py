def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr((char ** key) % n) for char in ciphertext]
    return plain

private_key = (2753, 3233)  

# 整數列表
ciphertext = [612, 745, 1632, 487, 624, 1175, 1794, 538, 538, 538]

decrypted_message = decrypt(private_key, ciphertext)
print("Decrypted message is :", ''.join(map(lambda x: str(x), decrypted_message)))