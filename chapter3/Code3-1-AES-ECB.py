# NEVER USE: ECB is not secure!
from cryptography.hazmat.primitives.ciphers import Cipher,algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

key = os.urandom(16)
key = b"\x81\xff9\xa4\x1b\xbc\xe4\x84\xec9\x0b\x9a\xdbu\xc1\x83"
aesCipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
aesEncryptor = aesCipher.encryptor()
aesDecryptor = aesCipher.decryptor()

print(aesEncryptor.update(b'alice'))
print(aesEncryptor.update(b'bob'))
print(aesEncryptor.update(b'bob'))
print(aesEncryptor.update(b'bob'))
print(aesEncryptor.update(b'bob'))
'''print(aesDecryptor.update(aesEncryptor.update(b'this is aes ecb mode test')))
encText = aesEncryptor.update(b"a secret message")
decText = aesDecryptor.update(encText)
print(encText)
print(decText)'''


