from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken
import logging

# generate key for encryption and decryption
def generate_key():
    key = Fernet.generate_key()
    return key
# encrypt data using key
def encrypt_data(key, message):     
    fernet = Fernet(key)
    encMessage = fernet.encrypt(message.encode())
    return encMessage
# decrypt data using key
def decrypt_data(encMessage, key):
    fernet = Fernet(key)
    try:
        decMessage = fernet.decrypt(encMessage).decode()
        return decMessage
    except InvalidToken as e:
        logging.error(f"Decryption error: {e}")
        return None

if __name__ == "__main__":
    message = "hacker"
    # Optional: Print original message (for debugging purposes)
    print("message to be encrypted:",message)
    key = generate_key()
    # Optional: Print the key (for debugging purposes)
    # print(key.decode())
    
    encMessage = encrypt_data(key, message)
    # Optional: Print the encrypted message (for debugging purposes)
    print("message after encryption: ",encMessage.decode())
    
    decMessage = decrypt_data(encMessage, key)
    if decMessage is not None:
        # Optional: Print the decrypted message (for debugging purposes)
        print("message after decryption: ",decMessage)
    