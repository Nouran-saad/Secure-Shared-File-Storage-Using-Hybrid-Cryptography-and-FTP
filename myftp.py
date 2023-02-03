import ftplib
# FTP server credentials
FTP_HOST = "127.0.0.1"
FTP_PORT = 6060
FTP_USER = "username"
FTP_PASS = "P@ssw0rd"
# connect to the FTP server
def upload(filename):
    ftp = ftplib.FTP()
    ftp.connect(FTP_HOST,FTP_PORT)
    ftp.login(FTP_USER,FTP_PASS)
# force UTF-8 encoding
    ftp.encoding = "utf-8"
# local file name you want to upload
    #filename = "keys_output.txt"
    with open(filename, "rb") as file:
        ftp.storbinary(f"STOR "+filename, file)
# quit and close the connection
    #ftp.dir()
    ftp.quit()
