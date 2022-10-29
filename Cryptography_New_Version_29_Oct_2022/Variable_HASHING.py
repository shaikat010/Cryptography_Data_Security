
import hashlib

print(hashlib.algorithms_available)

print(hashlib.algorithms_guaranteed)

hash = hashlib.new('md4')
hash.update(b'Python is Here!')

print(hash)


# gives the digest from the hashing
x = hash.digest()
print(x)

# gives the hex digest in the hexadecimal format
y = hash.digest()
print(y)

# finding the block size:
size = hash.block_size
print(size)
print(size)

# finding the digest size:
size = hash.digest_size
print(size)

# check that the digest size is smaller than the block size.


