from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from base64 import b64decode



encrypted_data_from_user = 'EXk9bafvI/tvHUtCJtuds8R617WVPtRNOspgCq4BKazt6TNJ3mRNaHnUDbEzRzLyOgDKHuILSj39LUwuMepz0vTkGQ4dU0SUtIVMUOYCxb/azDgK7ScCdSUfcWmtjNHwFGt+TneAn+KGuLRkWET45sivqJe0ozgBnNDbySlireo='
f = open('privatekey.pem', 'rb')
my_private_key = f.read()
f.close()
key = RSA.importKey(my_private_key)

cipher = PKCS1_OAEP.new(key, hashAlgo=SHA256)

decrypted_message = cipher.decrypt(b64decode(encrypted_data_from_user))
print(decrypted_message)