# Caesar cipher
As part of the OsloMet course: "Problem-Solving with Scripting"

## What is a Caesar Cipher?
A caesar cipher encrypts a word by replacing each letter with a fixed number position somewhere down the alphabet.
For example, with a letter shift of 6, the letter A would be replaced by the letter G.

The caesar cipher is known to be one of the easiests and most known ways of encryption.

### My solution
I use Python objects to recreate the Caesar Cipher, the object is called *CaesarCipher* and has a required parameter: *seed*. The *seed* will create a ciphered alphabet which the program uses to decrypt and encrypt messages. The object has two methods:

#### .encrypt(message)
Converts the message to a Caesar Cipher using the **seed** defined when initialising the cipher object
___

#### .decrypt(message)
Decrypts the message argument to a understandable string / sentence
___
