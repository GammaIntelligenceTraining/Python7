import hashlib
password = '12345678'

pass_hash = hashlib.md5(password.encode('utf-8')).hexdigest()[:5]  # 25d55

password2 = '12345678199360'
pass_hash1 = hashlib.md5(password2.encode('utf-8')).hexdigest()[:5]
print(pass_hash)
print(pass_hash1)