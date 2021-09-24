import chapter1.ShiftCipherApplication as sca

print(sca.__name__)
encoding, decoding = sca.create_shift_substitution(2)
print(encoding)
print(decoding)
plain = 'Hello world!'
c = sca.encode(plain.upper(), encoding)
print(c)
#p = sca.decode(c, decoding)
#print(p)

#生成所有的加密解密代换表；并使用每一个解密代换表解密密文
'''for i in range(26):
    encoding, decoding = sca.create_shift_substitution(i)
    p = sca.decode(c,decoding)
    print(p)'''









