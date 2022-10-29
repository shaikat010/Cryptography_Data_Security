import hashlib
hash = hashlib.md5(b'Hello Python')
Encrypted_Data = hash.digest()
Encrypted_Hex_Data = hash.hexdigest()
print(Encrypted_Data)
print(Encrypted_Hex_Data)

Block_Size = hash.block_size
print(Block_Size)

Digest_Size = hash.digest_size
print(Digest_Size)

#what is block size and digest size
