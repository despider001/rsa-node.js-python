var forge = require('node-forge')
var publicKey = forge.pki.publicKeyFromPem('-----BEGIN PUBLIC KEY-----MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCgm00biwxsKu/vCr0ETN/q5ZNXxlfbzYcJY32Cd0iUDQLVekoXqTCLSlndxd216pkoHgMXgDctujx5zVkRfhKIM0CVey2vwIjpLsBqm6TFtgv2sThkQT2HMwpjHmThZaPXFqfVtDFVt+as0CRvqJm3z/jdeMgSvFSvlJszRwqSuwIDAQAB-----END PUBLIC KEY-----');
var secretMessage = "user input goes here";

var encrypted = publicKey.encrypt(secretMessage, "RSA-OAEP", {
            md: forge.md.sha256.create(),
            mgf1: forge.mgf1.create()
        });

var base64 = forge.util.encode64(encrypted);
console.log(base64);