
import hashlib

sha = hashlib.sha1(b'Python').digest()
print("This is the SHA1 encrypted data: " + str(sha))



