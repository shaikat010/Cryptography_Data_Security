import hashlib

#the ones avaiable in your system
print(hashlib.algorithms_available)

#the onces avaiable in hashlib
print(hashlib.algorithms_guaranteed)

hashed_string = hashlib.sha224((b'Hello World'))
encrypted_string = hashed_string.digest()
encrypted_hex_string = hashed_string.hexdigest()
print("The ecrpted data is: " + str(encrypted_string))
print("The ecrpted data is: " + str(encrypted_hex_string))

#you can also use other stringer SHA versions which are avaiable



