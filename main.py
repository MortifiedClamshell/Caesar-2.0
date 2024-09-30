def caesar_cipher_encrypt(text, shift):
    result = ""
    
    for char in text:
        if char.islower():
            # Shift lowercase letters and transform to uppercase
            new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('A'))
        elif char.isupper():
            # Shift uppercase letters and transform to lowercase
            new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('a'))
        elif char.isdigit():
            # Shift digits and transform to letters
            new_char = chr((ord(char) - ord('0') + shift) % 10 + ord('0'))
        else:
            # Leave other characters unchanged
            new_char = char
        
        result += new_char
    
    return result

def caesar_cipher_decrypt(text, shift):
    result = ""
    
    for char in text:
        if char.islower():
            # Shift lowercase letters and transform to uppercase
            new_char = chr((ord(char) - ord('a') - shift) % 26 + ord('A'))
        elif char.isupper():
            # Shift uppercase letters and transform to lowercase
            new_char = chr((ord(char) - ord('A') - shift) % 26 + ord('a'))
        elif char.isdigit():
            # Shift digits and transform to letters
            new_char = chr((ord(char) - ord('0') - shift) % 10 + ord('0'))
        else:
            # Leave other characters unchanged
            new_char = char
        
        result += new_char
    
    return result

# Example usage
text = "abcdwxyzABCDWXYZ123890"
shift = 3
ciphered_text = caesar_cipher_encrypt(text, shift)
deciphered_text = caesar_cipher_decrypt(ciphered_text, shift)

print("Original text:", text)
print("Ciphered text:", ciphered_text)
print("Deciphered text:", deciphered_text)
