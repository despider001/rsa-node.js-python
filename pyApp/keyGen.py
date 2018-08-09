from Crypto.PublicKey import RSA

# 1024 means the keysize will be 1024 bits

key_pair = RSA.generate(1024)

private_key = open("privatekey.pem", "w")

private_key.write(key_pair.exportKey())

private_key.close()

public_key = open("public_key.pem", "w")

public_key.write(key_pair.publickey().exportKey())

public_key.close()