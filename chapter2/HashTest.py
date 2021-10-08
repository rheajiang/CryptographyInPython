import hashlib
import os
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend
import bcrypt

md5hasher = hashlib.md5(b'')
print(md5hasher.hexdigest())

md5hasher.update(b'a')
md5hasher.update(b'l')
md5hasher.update(b'i')
md5hasher.update(b'c')
md5hasher.update(b'e')
print(b'a')
print('a')
print(md5hasher.hexdigest())


str = '你好'
utf8 = str.encode('utf-8')
print(utf8)
str1 = utf8.decode()
print(str1)


md5hasher = hashlib.md5(b'alice')
print(md5hasher.hexdigest())
sha1hasher = hashlib.sha1(b'alice')
print(sha1hasher.hexdigest())

#scrypt 口令加盐
salt = os.urandom(16)

kdf = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1,backend=default_backend())
key = kdf.derive(b'my great password')
#print('加盐后的口令是：{}'.format(key.decode('ISO-8859-1')))
#print('加盐后的口令是：{}'.format(key))
print(key)


kdf = Scrypt(salt =salt, length =32, n=2**14, r=8, p=1, backend=default_backend())
kdf.verify(b"my great password", key)
print("Success! (Exception if mismatch)")

#bcypt 口令加盐
passwd = '123456'

# 口令加密过程
salt = bcrypt.gensalt(rounds=10)
hashed = bcrypt.hashpw(passwd.encode(), salt)
#str.encode()将字符串转换为字节数组
#字节数组转换为字符串使用bytes.decode()

print(salt)
# b'$2b$12$BlfmESsgNnsQFCmpUnhDWO'

print(hashed)
# b'$2b$12$BlfmESsgNnsQFCmpUnhDWO2RbacoHJViT8AZR1qh3DDOHnZxB.J5q'

# 校验过程
ret = bcrypt.checkpw(passwd.encode(), hashed)

print(ret)
# True




