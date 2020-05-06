# RSA_node_py

### Fork the repo or simply clone it
- [x] `git clone https://github.com/despider001/rsa-node.js-python.git`

### Generate publicKey and privateKey from the python client
- [x] generate publicKey and privateKey (`python /RSA_node_py/pyApp/keyGen.py`)
- [x] copy the publicKey from `/RSA_node_py/pyApp/public_key.pem`

### Let's encrypt your secret msg
- [x] `cd /RSA_node_py/App/`
- [x] `npm install`
- [x] paste the publicKey in  `/RSA_node_py/App/app.js` >> `var publicKey = forge.pki.publicKeyFromPem('--publicKey-goes-here--');`
- [x] set the msg you want to encrypt >> `var secretMessage = "user input goes here";`
- [x] `node app.js`
- [x] copy the code from console (this is the encrypted msg, which could only be opened by the publicKey provider, with his privateKey)

### Finally, let's decrypt the secret msg
- [x] paste the encrypted msg in `/RSA_node_py/pyApp/decrypt.py ` >> `encrypted_data_from_user ='--encrpted-msg-goes-here--'`
- [x] now `python /RSA_node_py/pyApp/decrypt.py` should print the decrypted msg!

