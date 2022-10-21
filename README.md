# Cryptography_Data_Security
Contains code for the cryptography practise coding. The codes contain cryptography codes for symmetric and asymmetric cryptography.

![image](https://user-images.githubusercontent.com/68814937/194497417-dec71caf-4472-4d5d-bc0b-71adec30b7b7.png)


# What is Cryptography?
Cryptography is associated with the process of converting ordinary plain text into unintelligible text and vice-versa. It is a method of storing and transmitting data in a particular form so that only those for whom it is intended can read and process it. Cryptography not only protects data from theft or alteration, but can also be used for user authentication.

# What is cryptosystem?
The whole system whereby the encrypption and decryption occurs, the key configuration and all the algorithms combined is called the cryptosystem

# Types of cryptography
The 2 major types of cryptography are the public and private key cryptography. 

Three types of cryptographic techniques used in general.

1. Symmetric-key cryptography

2. Hash functions.

3. Public-key cryptography

Symmetric-key Cryptography: Both the sender and receiver share a single key. The sender uses this key to encrypt plaintext and send the cipher text to the receiver. On the other side the receiver applies the same key to decrypt the message and recover the plain text.

Public-Key Cryptography: This is the most revolutionary concept in the last 300-400 years. In Public-Key Cryptography two related keys (public and private key) are used. Public key may be freely distributed, while its paired private key, remains a secret. The public key is used for encryption and for decryption private key is used.

Hash Functions: No key is used in this algorithm. A fixed-length hash value is computed as per the plain text that makes it impossible for the contents of the plain text to be recovered. Hash functions are also used by many operating systems to encrypt passwords.

# Cryptalgorithms
There are several crypto algorithms or as they are generally called, cipher. There ar several known ciphers such as DES and AES and the RSA and DSA algorithms too. SOme of these cipher can been cracked and can no longer be in use due to security reasons while others are still being tested to be used in mass network data communication in the near future.

# Authentication and Authorization

![image](https://user-images.githubusercontent.com/68814937/194498245-c4f59222-e0be-4b49-b83d-a1ee06b5ec27.png)



# SSL Protections
For the encryption process the client uses the server’s public key which is used to encrypt all the data.
Authenticity is provided via securing the right client and the server connection
For client auth, the server uses a public key in the client certificate,
If any of the steps fail then the handshake fails,
SSL provides integrity of data by encryption of data flow by using hash algorithms,
A combination of symmetric and asymmetric encryption is used to perverse the confidentiality of the information being transferred,
During a SSL handshake, the client and the server will both agree to encryption algorithm and a private key, 

# Sub-Protocols in SSL 
Record layer Protocol → confidentiality and message integrity,
Data is divided into fragments, the fragments comprises of the fragmented SHA code and the MD5 code,
After the encryption of the data is done, the last SHA header is also appended to the data,
Next is the 4 phase handshake protocol
1 → Both the client and server sends hello packets to each other,
2 → They exchange the certificates with the private and public key,
3 → They reply to each other by the encryption algorithms and the secret keys,
4 → The handshake is completed,
Next is the Change Cipher Spec Protocol:
For this protocol we use a part of the SSL Record protocol,
Consists of a single message of one byte,
Used to convey alert messages to the peer entity,


SSL 2.0 and 3,0 has been deprecated, and the TLS was developed as a successor,

# Deffie Hellman Key Exchange: 
Need a secure channel for communication,
Use the algorithm for exchange of keys over insecure channels,
Uses a one way function,
 Example already in codes,


# Application of Deffie Hellman Key Exchange:
Public Key Infrastructure,
SSL/TLS handshake
Secure Shell Access, used to access the system terminals,


# Public Key Infrastructure Components:
Certificate Authority → issue key
Verification Authority, → Validates key
Registration Authority, → request the registration auth for a signature,
Sender,
Recipient,

![image](https://user-images.githubusercontent.com/68814937/197285049-77e5cbc3-5d8a-4ead-aa6a-61c8527b8a6b.png)


