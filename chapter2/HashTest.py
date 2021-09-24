import hashlib
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


