# imports the string module for getting alphabet
import string

class CaesarCipher():
    
    alphabet = string.ascii_lowercase
    
    def __init__(self, seed):
        self.seed = seed
        # constructs a ciphered alphabet from the seed set by the user
        self.cipher_alphabet = self.alphabet[self.seed:] + self.alphabet[0:self.seed]
    
    def encrypt(self, message):
        # goes through the message and encrypts it using the index position of each letter in the original alphabet.
        encrypted_msg = ""
        for char in message:
            encrypted_msg += self.cipher_alphabet[(self.alphabet.index(char))]
        return encrypted_msg
    
    def decrypt(self, message):
        # reverses the process of encryption by using the ciphered alphabet index in the original alphabet.
        decrypted_msg = ""
        for char in message:
            decrypted_msg += self.alphabet[(self.cipher_alphabet.index(char))]
        return decrypted_msg
    
    def __repr__(self):
        return f"The seed for this cipher is {self.seed}"