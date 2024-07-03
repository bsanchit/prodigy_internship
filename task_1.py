def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    
    return encrypted_text


def caesar_cipher_decrypt(text, shift):
    """    
    Returns:
    str: The decrypted text.
    """
    decrypted_text = ""
    
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - shift_base - shift) % 26 + shift_base)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    
    return decrypted_text


def main():
    choice = input("Would you like to (E)ncrypt or (D)ecrypt a message? ").upper()
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))
    
    if choice == 'E':
        encrypted_message = caesar_cipher_encrypt(message, shift)
        print(f"Encrypted Message: {encrypted_message}")
    elif choice == 'D':
        decrypted_message = caesar_cipher_decrypt(message, shift)
        print(f"Decrypted Message: {decrypted_message}")
    else:
        print("Invalid choice! Please enter 'E' for encryption or 'D' for decryption.")

if __name__ == "__main__":
    main()
