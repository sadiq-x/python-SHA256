import hashlib
hashStr = str(input('Hash for:'))
hashedStr = hashlib.sha256(hashStr.encode('utf-8')).hexdigest()
print(hashedStr)