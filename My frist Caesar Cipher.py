import random
import string


def generate_password():
    # Define the characters to use
    letters = string.ascii_letters
    digits = string.digits

    # Ensure the password has at least 10 characters and at least 2 digits
    while True:
        # Randomly choose 8 letters and 2 digits to ensure at least 2 digits are present
        random_letters = random.choices(letters, k=7)
        random_digits = random.choices(digits, k=3)
        password_list = random_letters + random_digits

        # Shuffle the characters to randomize the letters and numbers
        random.shuffle(password_list)

        # Combine the list into a single string
        password = ''.join(password_list)

        # Check if the password meets the length requirement
        if len(password) >= 10:
            return password

# Generate a password
print("Generated Password:", generate_password())
