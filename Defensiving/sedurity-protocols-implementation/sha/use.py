import hashlib
from sha256 import generate_hash

print(generate_hash("Hello").hex())
print(hash=hashlib.sha256(b"Hello").hexdigest())
