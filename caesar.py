import string

class CaesarCipher():
    
    alphabet = string.ascii_lowercase
    
    def __init__(self, seed):
        self.seed = seed
        self.cipher_alphabet = self.alphabet[self.seed:] + self.alphabet[0:self.seed]
    
    def encrypt(self, message):
        encrypted_msg = ""
        for char in message:
            encrypted_msg += self.cipher_alphabet[(self.alphabet.index(char))]
        return encrypted_msg
    
    def decrypt(self, message):
        decrypted_msg = ""
        for char in message:
            decrypted_msg += self.alphabet[(self.cipher_alphabet.index(char))]
        return decrypted_msg
    
    def __repr__(self):
        return f"The seed for this cipher is {self.seed}"