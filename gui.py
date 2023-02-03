import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog,messagebox
import myftp , ftp_download,security,keys_symmetric_ciphers


r = tk.Tk()
r.title('Secure-Shared-File-Storage')
r.rowconfigure(0, minsize=800, weight=1)
r.columnconfigure(1, minsize=800, weight=1)
frm_buttons = tk.Frame(r, relief=tk.RAISED, bd=2)

def choose_file_to_encrypt():
        filePath=filedialog.askopenfilename()
        return filePath
def encrypt_file_and_keys():
    key_des=keys_symmetric_ciphers.generate_des_key()
    key_aes=keys_symmetric_ciphers.generate_aes_key()
    key_rc2=keys_symmetric_ciphers.generate_RC2_key()
    messagebox.showinfo("Information","Choose file to encrypt")
    filePath=choose_file_to_encrypt()
    security.round_robin_enc(key_des,key_aes,key_rc2,filePath)
    security.write_keys_file(key_des,key_aes,key_rc2)
    key_blowfish=keys_symmetric_ciphers.generate_blowfish_key()
    security.encrpt_BLOWFISH(key_blowfish,"keys.txt","keys_output.txt")
    security.write_key_blowfish(key_blowfish)
    security.encrypt_master_key(key_blowfish)
    toplevel = Toplevel(r)
    label1 = Label(toplevel, text='file and keys are encrypted', height=0, width=100)
    label1.pack()

def upload_files():
    encrypt_file_and_keys()
    messagebox.showinfo("Information","Choose the encrypted file to upload")
    file=filedialog.askopenfilename()
    filename=os.path.basename(file)
    myftp.upload(filename)
    messagebox.showinfo("Information","Choose the encrypted keys file to upload")
    file2=filedialog.askopenfilename()
    filename2=os.path.basename(file2)
    myftp.upload(filename2)
    messagebox.showinfo("Information","Choose the encrypted masterkey file to upload")
    file3=filedialog.askopenfilename()
    filename3=os.path.basename(file3)
    myftp.upload(filename3)
    toplevel = Toplevel(r)
    label1 = Label(toplevel, text='Uploaded', height=0, width=100)
    label1.pack()
    
def decypt_file_and_keys():
    security.decrypt_master_key()
    with open ('masterkey_dec.txt','rb') as masterout:
        key_blowfish= masterout.read()
    security.decrpyt_BLOWFISH(key_blowfish,"keys_output.txt","keys.txt")
    with open ('keys.txt','rb') as masterout:
        key_des= masterout.read(8)
        key_aes=masterout.read(16)
        key_rc2=masterout.read(8)
        messagebox.showinfo("Information","Choose the decrypted file to see the content")
    filePath=choose_file_to_encrypt()
    security.round_robin_dec(key_des,key_aes,key_rc2,filePath)
    with open (filePath,'rb') as inn:
        value=inn.read()
    label2 = Label(r, text= "The decrypted file content:" +str(value), wraplength=500 ).place(x=240,y=90)
    
def download_files():
    ftp_download.download('output.txt')
    ftp_download.download('keys_output.txt')
    ftp_download.download('masterkey_enc.txt')
    toplevel = Toplevel(r)
    label1 = Label(toplevel, text='Downloaded', height=0, width=100)
    label1.pack()
    decypt_file_and_keys()
    





button_upload = tk.Button(frm_buttons, text='Upload', width=25, command=lambda:upload_files())
button_download = tk.Button(frm_buttons, text='Download', width=25, command= lambda:download_files())
stop = tk.Button(frm_buttons, text='Stop', width=25, command=r.destroy)
button_upload.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
button_download.grid(row=2, column=0, sticky="ew", padx=5)
stop.grid(row=4, column=0, sticky="ew", padx=5)

frm_buttons.grid(row=0, column=0, sticky="ns")



r.mainloop()