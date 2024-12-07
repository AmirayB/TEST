import hashlib
data="hello world"
# Create a SHA-256 hash object
sha256_hash = hashlib.sha256()

# Update the hash object with the data (must be encoded to bytes)
sha256_hash.update(data.encode('utf-8'))

# Get the hexadecimal digest of the hash
hash_digest = sha256_hash.hexdigest()

print("Original data:", data)
print("SHA-256 hash:", hash_digest)