# securitytools

## Summary
Security tools created using python
1. Keylogger - (Script - keylogger.py)
2. Ceasar Cipher code to Encrypt/Decrypt text <br>
   a. "CipherCeasarSalad.py" is command line Ceasar cipher tool <br />
   b. "CipherCeasarSaladWeb.py" is web bases Ceasar cipher tool <br />
   c. This has complete implementation where encryption and decryption,along with alphabets characters, also
   performed for key space, numerical, special characters
3. Hashing Password used SHA256 hash algorithm to hash the password. <br />
   a. Storing username and hash password on SQLite DB. <br />
   b. The Salt generated is stored on the different table to maintain the integrity and confidentiality - 
   (Script - HashMyPassword.py, DB - security.db) <br />
4. Packet Crafting (Script - PacketCrafting.py)   <br />
   a. Implemented "XMAS" attack <br />
   b. Custom crafted TCP three way handshake
5. Vulnerability Scanner (Please visit "vulneabilityscanner" folder for more deatils)

### Pre-requisities
1. Install Python 3.9 
2. Run "pip install -r requirements.txt"

Following is UI for Ceasar Cipher
![alt text](https://github.com/virenukey/securitytools/blob/main/UI_For_Ceasar_Cipher.PNG?raw=true)

Following is Wireshark screenshot for the ananlyzing XMAS attack using "PacketCrafting.py"
![alt text](https://github.com/virenukey/securitytools/blob/main/xmas-attack.PNG?raw=true)