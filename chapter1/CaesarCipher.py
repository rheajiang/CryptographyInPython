# -*- coding: utf-8 -*-

class CaesarCipher(object):
    """
    凯撒加密解密
    """

    def __crypt(self, char, key):
        """
        对单个字母加密，偏移
        @param char: {str} 单个字符
        @param key: {num} 偏移量
        @return: {str} 加密后的字符
        """
        if not char.isalpha():
            return char
        else:
            base = "A" if char.isupper() else "a"
            return chr((ord(char) - ord(base) + key) % 26 + ord(base))

    def encrypt(self, char, key):
        """
        对字符加密
        """
        return self.__crypt(char, key)

    def decrypt(self, char, key):
        """
        对字符解密
        """
        return self.__crypt(char, -key)

    def __crypt_text(self, func, text, key):
        """
       对文本加密
       @param char: {str} 文本
       @param key: {num} 偏移量
       @return: {str} 加密后的文本
       """
        lines = []
        for line in text.split("\n"):
            words = []
            for word in line.split(" "):
                chars = []
                for char in word:
                    chars.append(func(char, key))
                words.append("".join(chars))
            lines.append(" ".join(words))
        return "\n".join(lines)

    def encrypt_text(self, text, key):
        """
        对文本加密
        """
        return self.__crypt_text(self.encrypt, text, key)

    def decrypt_text(self, text, key):
        """
        对文本解密
        """
        return self.__crypt_text(self.decrypt, text, key)


if __name__ == '__main__':
    plain = """
    Hello cryptography!
    """
    key = 3

    cipher = CaesarCipher()

    # 加密
    c = cipher.encrypt_text(plain, key)
    print(c)
    # Khoor fubswrjudskb!

    # 解密
    print(cipher.decrypt_text(c, key))
    # Hello cryptography!

