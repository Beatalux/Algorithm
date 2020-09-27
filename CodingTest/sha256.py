import hashlib

str = input()
array = hashlib.sha256(str.encode())

print(array.hexdigest())
