

# shake is one of the hashing algorithm,
# the digest in the shake algorithm can be of variable length,


import hashlib

print(hashlib.algorithms_available)

# this is the hash object
hash = hashlib.shake_256(b'Hello World!')
print(hash)


x = hash.digest(12)
print(x)

# hex digest of 10 size
y = hash.hexdigest(10)
print(y)

# increasing the size of the digest
y = hash.hexdigest(10)
print(y)

# shake_128 can be also used instead of the shake_256



