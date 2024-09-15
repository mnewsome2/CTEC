import random
import string


def generate_password():
    """Generate a random password with at least 10 characters and at least 2 digits."""
    letters = string.ascii_letters
    digits = string.digits

    while True:
        random_letters = random.choices(letters, k=8)
        random_digits = random.choices(digits, k=2)
        password_list = random_letters + random_digits
        random.shuffle(password_list)
        password = ''.join(password_list)

        if len(password) >= 10:
            return password


def caesar_cipher(text, key, encrypt=True):
    """Encrypts or decrypts a text using Caesar Cipher with the given key."""
    result = ""
    shift = key if encrypt else -key

    for char in text:
        if char.isalpha():  # Check if the character is a letter
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        elif char.isdigit():  # Check if the character is a digit
            result += chr((ord(char) - ord('0') + shift) % 10 + ord('0'))
        else:
            result += char  # Non-alphabetic and non-numeric characters remain unchanged
    return result


# Generate a random password
random_password = generate_password()
print("Generated Password:", random_password)

# Encrypt the password using Caesar Cipher
encryption_key = 3  # Example shift key for Caesar Cipher
encrypted_password = caesar_cipher(random_password, encryption_key, encrypt=True)
print("Encrypted Password:", encrypted_password)

# Decrypt the password using Caesar Cipher
decrypted_password = caesar_cipher(encrypted_password, encryption_key, encrypt=False)
print("Decrypted Password:", decrypted_password)

# User input for message encryption and decryption
user_message = input("Enter a message to encrypt: ")
user_key = 3

# Encrypt user message using Caesar Cipher
encrypted_message = caesar_cipher(user_message, user_key, encrypt=True)
print("Encrypted Message:", encrypted_message)

# Decrypt user message using Caesar Cipher
decrypted_message = caesar_cipher(encrypted_message, user_key, encrypt=False)
print("Decrypted Message:", decrypted_message)
