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


## Test Cases
There are 3 test cases to encrypt and decrypt 3 different text files (input(small-size file) , input2 (medium-size file) , input3 (large-size file)with different sizes and python file (min_temp_dataframe.py). 

### Example of one of the testcases ( input(small-size file) )

#### When press the upload button
![image](https://user-images.githubusercontent.com/55962261/216706972-adf2c0ae-317a-4189-abcf-f249dbcb753f.png)
![image](https://user-images.githubusercontent.com/55962261/216707021-bcc425ae-8cab-49a2-b63a-bfa948281bd8.png)
![image](https://user-images.githubusercontent.com/55962261/216707046-5c1a7756-9f6e-4913-8113-c541c57ab36f.png)
![image](https://user-images.githubusercontent.com/55962261/216707080-e0c2f389-bc82-4b22-a2ae-1ad5a79c7d62.png)
![image](https://user-images.githubusercontent.com/55962261/216707100-38d11631-9193-416d-970c-9647f750e133.png)
![image](https://user-images.githubusercontent.com/55962261/216707142-b4e392ec-5110-482b-96d7-c9e0dbe1cbe4.png)
![image](https://user-images.githubusercontent.com/55962261/216707199-83ddde48-f2e5-41f8-8024-e6b366a62225.png)
![image](https://user-images.githubusercontent.com/55962261/216708137-551c84bb-75ae-4a50-b680-2f92695df7d3.png)
#### When Press Download
![image](https://user-images.githubusercontent.com/55962261/216707347-0f327c46-2b66-479a-830e-815516ca16ae.png)
![image](https://user-images.githubusercontent.com/55962261/216708078-dddbc9b2-c509-4c12-922e-b0d9b0cadda8.png)
![image](https://user-images.githubusercontent.com/55962261/216707395-5fb9bba0-5016-4bc7-91bf-dddf049e8c4d.png)
#### Press Stop button To destroy the window
![image](https://user-images.githubusercontent.com/55962261/216707431-b8d9d490-4850-4f08-a369-00a99d60a59f.png)
