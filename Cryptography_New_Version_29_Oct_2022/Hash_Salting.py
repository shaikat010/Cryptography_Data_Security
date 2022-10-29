
import hashlib, binascii

#pbkdf2_hmac uses some kind of pseudorandomness
# 100 is the number of iteration
hash = hashlib.pbkdf2_hmac('sha512',b'Hello World 123!', b'salt the password', 1000)
print(hash)
x = binascii.hexlify(hash)
print(x)

