import cryptography.fernet

# Generate a key for encryption and decryption
# Keep this key safe; if you lose it, you won't be able to decrypt the messages
key = cryptography.fernet.Fernet.generate_key()
print(f"Generated Key: {key.decode()}")

# Create a Fernet object with the key
cipher_suite = cryptography.fernet.Fernet(key)

# The message you want to encrypt
message = "This is my first secret message code".encode()

# Encrypt the message
encrypted_message = cipher_suite.encrypt(message)
print(f"Encrypted Message: {encrypted_message.decode()}")

# Decrypt the message
decrypted_message = cipher_suite.decrypt(encrypted_message)
print(f"Decrypted Message: {decrypted_message.decode()}")
