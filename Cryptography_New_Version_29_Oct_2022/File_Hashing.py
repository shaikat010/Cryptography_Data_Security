
import hashlib

filename = input("Enter the input file name: ")
with open(filename, "rb") as f:
    bytes = f.read()
    readable_hash = hashlib.sha256(bytes).hexdigest();
    print(readable_hash)

