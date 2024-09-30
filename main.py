def caesar_cipher_encrypt(text, shift):
    result = ""
    
    for char in text:
        if char.islower():
            # Shift lowercase letters and transform to numbers or beginning of uppercase letters
            new_char = chr((ord(char) - ord('a') + shift) % 10 + ord('0')) if (ord(char) - ord('a') + shift) < 10 else chr((ord(char) - ord('a') + shift - 10) % 26 + ord('A'))
        elif char.isupper():
            # Shift uppercase letters and transform to lowercase
            new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('a'))
        elif char.isdigit():
            # Shift digits and transform to remaining uppercase letters
            new_char = chr((ord(char) - ord('0') + shift) % 16 + ord('K'))
        else:
            # Leave other characters unchanged
            new_char = char
        
        result += new_char
    
    return result

def caesar_cipher_decrypt(text, shift):
    result = ""
    
    for char in text:
        if 'a' <= char <= 'z':
            # Reverse shift for lowercase letters transformed from uppercase
            new_char = chr((ord(char) - ord('a') - shift) % 26 + ord('A'))
        elif '0' <= char <= '9':
            # Reverse shift for numbers transformed from lowercase letters
            new_char = chr((ord(char) - ord('0') - shift) % 10 + ord('a')) if (ord(char) - ord('0') - shift) < 10 else chr((ord(char) - ord('0') - shift - 10) % 26 + ord('A'))
        elif 'K' <= char <= 'Z':
            # Reverse shift for uppercase letters transformed from digits
            new_char = chr((ord(char) - ord('K') - shift) % 16 + ord('0'))
        else:
            # Leave other characters unchanged
            new_char = char
        
        result += new_char
    
    return result

# Example usage
text = "abcdwxyzABCDWXYZ123890"
shift = 90 % 10
ciphered_text = caesar_cipher_encrypt(text, shift)
deciphered_text = caesar_cipher_decrypt(ciphered_text, shift)

print("Original text:", text)
print("Ciphered text:", ciphered_text)
print("Deciphered text:", deciphered_text)
