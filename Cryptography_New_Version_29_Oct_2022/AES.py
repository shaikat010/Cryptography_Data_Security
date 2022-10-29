#the key must 16,24,32 bytes long
#plain text should be in multiples of 16 bytes

# from Crypto.Cipher import AES
# key = b"Sixteen byte key"
# plain_text = 'Secret 16 bytes'
# Cipher = AES.new(key, AES.MODE_EAX )
# nonce = Cipher.nonce
# ciphertext, tag = Cipher.encrypt_and_digest(plain_text)
# #ciphertext = Cipher.encrypt(plain_text)
# print("Encrypted Text: " + ciphertext)

#The above does not work because there are issues woth the crypto package
#so in the code below we are uninstalling all libraries and then using the pycryptodome package library only!

#AES Encryption
#due to security issues with pycrypto package, pycryptodome is to be installed and this code is to be used
from Crypto.Cipher import AES
string = input("Enter string to encrypt: ")
plain_text = bytes(string, 'utf-8')
#plain_text = b'Random text to encrypt here'
key = b'Sixteen byte key'
cipher = AES.new(key, AES.MODE_EAX)

nonce = cipher.nonce
ciphertext, tag = cipher.encrypt_and_digest(plain_text)

#AES Decryption
key = b'Sixteen byte key'
cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
plaintext = cipher.decrypt(ciphertext)
try:
    cipher.verify(tag)
    print("The message is authentic:", plaintext)
except ValueError:
    print("Key incorrect or message corrupted")

