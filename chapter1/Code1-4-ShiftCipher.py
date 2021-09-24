#import sys
#sys.path.append(r'D:\Users\jyl\Documents\GitHub\CryptographyInPython\chapter2')
import chapter1.CCC as ccc

n = 2
A = ccc.A(n)
A.printable_substitution()
print(A.encode("DFSAJLFDSALJFJSDF"))
print(A.decode(A.encode("DFSAJLFDSALJFJSDF")))



'''
# 代码清单1-1 创建替换表
def create_shift_substitution(n):
    encoding = {}
    decoding = {}
    alphabet_size = len(string.ascii_uppercase)
    for i in range(alphabet_size):
        letter = string.ascii_uppercase[i]
        subst_letter = string.ascii_uppercase[(i+n)%alphabet_size]
        encoding[letter] = subst_letter
        decoding[subst_letter] = letter
    return encoding, decoding

#编码/加密
def encode(message, subst):
    cipher = ""
    for letter in message:
        if letter in subst:
            cipher += subst[letter]
        else:
            cipher += letter
    return cipher
#解码/解密
def decode(message, subst):
    return encode(message, subst)

#打印替换表
def printable_substitution(subst):
    # 将替换表（字典）按照第一个元素进行排序
    mapping = sorted(subst.items())
    # Then create two lines: source above, target beneath.
    alphabet_line = " ".join(letter for letter, _ in mapping)
    cipher_line = " ".join(subst_letter for _, subst_letter in mapping)
    return "{}\n{}".format(alphabet_line, cipher_line)

if __name__ == "__main__":
    n = 1
    encoding, decoding = create_shift_substitution(n)

    while True:
        print("\nShift Encoder Decoder")
        print("--------------------")
        print("\tCurrent Shift: {}\n".format(n))
        print("\t1. Print Encoding/Decoding Tables.")
        print("\t2. Encode Message.")
        print("\t3. Decode Message.")
        print("\t4. Change Shift")
        print("\t5. Quit.\n")
        choice = input(">> ")
        print()

        if choice == '1':
            print("Encoding Table:")
            print(printable_substitution(encoding))
            print("Decoding Table:")
            print(printable_substitution(decoding))

        elif choice == '2':
            message = input("\nMessage to encode: ")
            print("Encoded Message: {}".format(encode(message.upper(), encoding)))

        elif choice == '3':
            message = input("\nMessage to decode: ")
            print("Decoded Message: {}".format(decode(message.upper(), decoding)))

        elif choice == '4':
            new_shift = input("\nNew shift (currently {}): ".format(n))
            try:
                new_shift = int(new_shift)
                if new_shift < 1:
                    raise Exception("Shift must be greater than 0")
                else:
                    n = new_shift
                    encoding, decoding = create_shift_substitution(n)
            except ValueError:
                print("Shift {} is not a valid number.".format(new_shift))

        elif choice == '5':
            print("Terminating. This program will self destruct in 5 seconds .\n")
            break

        else:
            print("Unknown option {}.".format(choice))
            '''