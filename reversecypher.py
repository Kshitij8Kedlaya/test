def decrypt_rot13(ciphertext):
    decrypted_text = ""

    for m in ciphertext:
        if m.islower():
            if 'a' <= m <= 'm':
                shifted_char = chr(ord(m) + 13)
            elif 'n' <= m <= 'z':
                shifted_char = chr(ord(m) - 13)
        elif m.isupper():
            if 'A' <= m <= 'M':
                shifted_char = chr(ord(m) + 13)
            elif 'N' <= m <= 'Z':
                shifted_char = chr(ord(m) - 13)
        else:
            shifted_char = m

        decrypted_text += shifted_char

    return decrypted_text

# Example usage:
cipher_text = "Gur dhvpx oebja sbk whzcf bire gur ynml qbt."
plain_text = decrypt_rot13(cipher_text)
print(plain_text)
