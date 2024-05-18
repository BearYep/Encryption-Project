def encrypt(pk, plaintext):
    key, n = pk
    cipher = [(ord(char) ** key) % n for char in plaintext]
    return cipher

public_key = (17, 3233)  

#設定明文值
plain_text = 'play098222'

encrypted_message = encrypt(public_key, plain_text)
print("Encrypted message is ", encrypted_message)
