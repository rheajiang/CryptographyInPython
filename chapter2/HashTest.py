import hashlib
md5hasher = hashlib.md5()
md5hasher.update(b'a')
md5hasher.update(b'l')
md5hasher.update(b'i')
md5hasher.update(b'c')
md5hasher.update(b'e')
print(md5hasher.hexdigest())

md5hasher = hashlib.md5(b'alice')
print(md5hasher.hexdigest())
sha1hasher = hashlib.sha1(b'alice')
print(sha1hasher.hexdigest())


