import os
from Cryptodome.Cipher import DES,AES,ARC2,Blowfish,PKCS1_OAEP
from Cryptodome.PublicKey import RSA




key = RSA.generate(2048)
def generate_priv_rsa():

    private_key=key.export_key()
    f = open('privateKeyRSA.pem','wb+')
    f.write(private_key)
    f.close()

def generate_public_rsa():
    public_key=key.publickey().export_key()
    f = open('publicKeyRSA.pem','wb+')
    f.write(public_key)
    f.close()





def encrpt_des(k, in_filename):
    encryptor=DES.new(k,DES.MODE_ECB)
    if len (in_filename) % 8 != 0:
                    in_filename += b' ' * (8 - len(in_filename) % 8)
                    value_des=encryptor.encrypt(in_filename)    
    else:value_des=encryptor.encrypt(in_filename)
    return value_des

def decrpyt_des(k, in_filename):
    decryptor = DES.new(k, DES.MODE_ECB)
    plain_txt=decryptor.decrypt(in_filename)
    return plain_txt


def decrpyt_AES(k, in_filename):
    decryptor = AES.new(k, AES.MODE_ECB)
    plain_txt=decryptor.decrypt(in_filename)
    return plain_txt


def decrpyt_RC2(k, in_filename):
    decryptor = ARC2.new(k, ARC2.MODE_ECB)
    plain_txt=decryptor.decrypt(in_filename)
    return plain_txt


def encrpt_AES(k, in_filename):

    encryptor=AES.new(k,AES.MODE_ECB)


    if len (in_filename) % 16 != 0:
                    in_filename += b' ' * (16 - len(in_filename) % 16) 
                    value_aes=encryptor.encrypt(in_filename)    
    else:value_aes=encryptor.encrypt(in_filename)
    return value_aes


def encrpt_BLOWFISH(k, in_filename, out_filename=None,chuncksize=8):
    encryptor = Blowfish.new(k, Blowfish.MODE_ECB)
    with open (in_filename,'rb') as infile:   
        with open(out_filename, 'wb+') as outfile:
            while True:
                chunck = infile.read(chuncksize)
                if len(chunck) == 0:
                    break
                elif len (chunck) % 8 != 0:
                    chunck += b' ' * (8 - len(chunck) % 8)

                outfile.write(encryptor.encrypt(chunck))


def decrpyt_BLOWFISH(k, in_filename, out_filename=None,chuncksize = 8):
    if not out_filename:
        out_filename = os.path.splitext(in_filename)[0]

    with open (in_filename, 'rb') as infile:
        decryptor = Blowfish.new(k, Blowfish.MODE_ECB)

        with open (out_filename,'wb+') as outfile:
            while True:
                chunck = infile.read(chuncksize)
                if len(chunck) == 0:
                    break
                outfile.write(decryptor.decrypt(chunck))
                
def encrpt_RC2(k, in_filename):

    encryptor=ARC2.new(k,ARC2.MODE_ECB)


    if len (in_filename) % 8 != 0:
                    in_filename += b' ' * (8 - len(in_filename) % 8)
                    value_rc2=encryptor.encrypt(in_filename)
    else:value_rc2=encryptor.encrypt(in_filename)
    return value_rc2

def encrypt_RSA(message):
    generate_public_rsa()
    key=RSA.importKey(open('publicKeyRSA.pem').read())
    cipher = PKCS1_OAEP.new(key)
    ciphertext = cipher.encrypt(message)
    return ciphertext

def decrypt_RSA(cipher_txt):
    generate_priv_rsa()
    key=RSA.importKey(open('privateKeyRSA.pem').read())
    cipher = PKCS1_OAEP.new(key)
    message = cipher.decrypt(cipher_txt)
    return message

def round_robin_enc(key_des,key_aes,key_rc2,input):
    filesize=os.path.getsize(input)
    with open (input,'rb') as infile:
        with open('output.txt','wb+') as out:
            for index in range (0,filesize):
                if (index % 3) == 0:
                    plain= infile.read(8)
                    if plain:
                        cipher=encrpt_des(key_des, plain)
                        out.write(cipher)
                                                
                    else : break
                elif (index % 3) ==1:
                    plain=infile.read(16)
                    if plain:
                        cipher=encrpt_AES(key_aes, plain)
                        out.write(cipher)
                    else: break
                else:
                    plain=infile.read(8)
                    if plain:
                        cipher=encrpt_RC2(key_rc2, plain)
                        out.write(cipher)
                    else: break



def write_keys_file(key_des,key_aes,key_rc2):
    with open ('keys.txt','wb+') as i:
        i.write(key_des)
        i.write(key_aes)
        i.write(key_rc2)

def write_key_blowfish(key_blowfish):
    with open ('masterkey.txt','wb+') as masterin:
        masterin.write(key_blowfish)


def encrypt_master_key(key_blowfish):
    encrypted_master_key=encrypt_RSA(key_blowfish)
    with open ('masterkey_enc.txt','wb+') as masterin:
        masterin.write(encrypted_master_key)
    return encrypted_master_key

def decrypt_master_key():
    with open('masterkey_enc.txt','rb') as o:
        encrypted_master_key=o.read()
    decrypted_master_key=decrypt_RSA(encrypted_master_key)
    with open ('masterkey_dec.txt','wb+') as masterin:
        masterin.write(decrypted_master_key)

def round_robin_dec(key_des,key_aes,key_rc2,filePath):
    filesize2=os.path.getsize('output.txt')
    with open ('output.txt','rb') as infile:
        with open (filePath,'wb+') as outt:
            for index in range (0,filesize2):

                if (index % 3) == 0:
                    cipher= infile.read(8)
                    if cipher:
                        plain=decrpyt_des(key_des, cipher)
                        outt.write(plain)
                    else : break
                elif (index % 3) ==1:
                    cipher=infile.read(16)
                    if cipher:
                        plain=decrpyt_AES(key_aes, cipher)
                        outt.write(plain)
                    else: break
                else:
                    cipher=infile.read(8)
                    if cipher:
                        plain=decrpyt_RC2(key_rc2, cipher)
                        outt.write(plain)
                    else: break
