def encrypt(input_str):
    encrypted_str = []

    for char in input_str:
        # Encrypt lowercase letters
        if 'a' <= char <= 'z':
            encrypted_str.append(chr((ord(char) - ord('a') + 3) % 26 + ord('a')))
        # Encrypt uppercase letters
        elif 'A' <= char <= 'Z':
            encrypted_str.append(chr((ord(char) - ord('A') + 3) % 26 + ord('A')))
        # Leave other characters unchanged
        else:
            encrypted_str.append(char)

    return ''.join(encrypted_str)

test_string = "Hello, World!"
print(encrypt(test_string))

# Output: "Khoor, Zruog!"
