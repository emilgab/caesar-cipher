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
            if char == " ":
                encrypted_msg += " "
            else:
                encrypted_msg += self.cipher_alphabet[(self.alphabet.index(char.lower()))]
        print(encrypted_msg)
    
    def decrypt(self, message):
        # reverses the process of encryption by using the ciphered alphabet index in the original alphabet.
        decrypted_msg = ""
        for char in message:
            if char == " ":
                decrypted_msg += " "
            else:
                decrypted_msg += self.alphabet[(self.cipher_alphabet.index(char.lower()))]
        print(decrypted_msg)
    
    def __repr__(self):
        return f"The seed for this cipher is {self.seed}"
    
if __name__ == "__main__":
    seed_in = int(input("What should the seed (position fix) be? "))
    t = CaesarCipher(seed_in)
    print("Cipher created successfully! Seed: {} \n".format(t.seed))
    decision = input("Type ENC to encrypt a message or DEC to decrypt as message. ")
    if decision.lower() == "enc":
        raw_msg = input("What message do you want to encrypt? ")
        print("Your encrypted message is: ")
        t.encrypt(raw_msg)
    elif decision.lower() == "dec":
        enc_msg = input("What encrypted message do you want to decrypt? ")
        print("Your message decrypted reads: ")
        t.decrypt(enc_msg)
    