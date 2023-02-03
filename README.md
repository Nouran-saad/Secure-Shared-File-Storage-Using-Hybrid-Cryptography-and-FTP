# Secure-Shared-File-Storage-Using-Hybrid-Cryptography-and-FTP
Project Requirments:

## File Storage:
1. Dividing the file to upload into N parts. (N depends on the file size)
2. Generate m keys randomly, where m is the number of symmetric ciphers used (at least 3 ciphers
including DES and AES, and you may choose a third one or even your own cipher)
3. Encrypting all the parts of the file using one of the selected algorithms (Algorithm is changed with
every part in round robin fashion). And the parts are put together in a single file as ordered.
4. The keys for cryptography algorithms are then grouped in a key file and encrypted using a different
algorithm and the key for this algorithm is also generated randomly and is called the file master key.
5. The data file and the key file are than uploaded to the FTP server
6. A copy of the master key is kept in a local file with the file name to be shared.
This has to be done through a GUI APP with the entire process encapsulated in a single use-case that is “Secure
Upload”.

## File Retrieval:
1. A user requesting the master key must provide his public key to the owner
2. The owner then encrypts the master key of the requested file with the requesting user public key
and sends it to him
3. The user can then download the data file and the key file, decrypts the master key with his private
key and then decrypts the data file
Requesting the master key can be done outside your app, but the encrypted master key must be imported to
the application of the file retriever and used to decrypt the file

## Sceenshots of the GUI:
![image](https://user-images.githubusercontent.com/55962261/216705410-7c7384ed-c98a-4c3b-bac4-74dbf2610e19.png)
