def decrypt_caesar_cipher(ciphertext):
    decrypted_text = ""

    for char in ciphertext:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            decrypted_char = chr(((ord(char) - ord('a') - 3) % 26) + ord('a'))
            if is_upper:
                decrypted_char = decrypted_char.upper()
            decrypted_text += decrypted_char
        else:
            decrypted_text += char

    return decrypted_text

cipher_text = input("Enter:")
plain_text = decrypt_caesar_cipher(cipher_text)
print(plain_text)
