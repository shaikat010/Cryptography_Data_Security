

from Crypto.Cipher import AES

# key should be of 16, 24 or 32 bytes
key= 'Sixteen Code Key'

# The plaintext has also to be a multiple of 16 bytes
plaintext = 'Secret 16 bytes'

# if the key or the string is not of 16 bytes then it will do padding at the end

cipher = AES.new(key)

ciphertext = cipher.encrypt(plaintext)
print(ciphertext)


# due to issues in the crypto package it is unwise to use this script.

