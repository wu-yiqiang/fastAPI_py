import base64
from Crypto.Cipher import AES
keyValue = '12de3FGSDds2343fdfs454657vdfF'
'''
采用AES对称加密算法
'''
# str不是16的倍数那就补足为16位
def add_to_16(value: str):
    if len(value) == 16:
        return value
    if len(value) < 16:
        return value.ljust(16, '0')
    if len(value) > 16:
        return value[0:16]


# 加密
def encryptStr(key, text):
    # 初始化加密器
    aes = AES.new(bytes(add_to_16(key), 'utf-8'), AES.MODE_ECB)
    #先进行aes加密
    encrypt_aes = aes.encrypt(bytes(text, encoding="utf-8"))
    #用base64转成字符串形式
    encrypted_text = str(base64.encodebytes(encrypt_aes))  # 执行加密并转码返回bytes
    return encrypted_text


# 解密
def decryptStr(key: str, text: str):
    # 初始化加密器
    aes = AES.new(bytes(add_to_16(key), encoding='utf-8'), AES.MODE_ECB)
    #优先逆向解密base64成bytes
    base64_decrypted = base64.decodebytes(text.encode(encoding='utf-8'))
    print("aes", aes.decrypt(base64_decrypted))
    decrypted_text = str(aes.decrypt(base64_decrypted), encoding='utf-8')
    return decrypted_text.strip()
