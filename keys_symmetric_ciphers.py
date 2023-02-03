from secrets import token_bytes
def generate_des_key():
    key_DES = token_bytes(8)
    return key_DES
def generate_RC2_key():
    key_RC2 = token_bytes(8)
    return key_RC2
def generate_blowfish_key():    
    key_blowfish = token_bytes(8)
    return key_blowfish
def generate_aes_key():
    key_AES = token_bytes(16)
    return key_AES
