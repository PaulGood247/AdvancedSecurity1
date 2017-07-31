import rsa
from pprint import pprint
from time import gmtime, mktime
from OpenSSL import crypto, SSL
from socket import gethostname

CERT_FILE = "selfsignedTest.crt"
KEY_FILE = "privateTest.key"


print("Generating keys...")
(pubkey, privkey) = rsa.newkeys(2048)
print(pubkey)
print(privkey)

message = 'Go left at the blue tree'
signature = rsa.sign(message, privkey, 'SHA-1')
rsa.verify(message, signature, pubkey)

cert = crypto.X509()
cert.get_subject().C = "UK"
cert.get_subject().ST = "London"
cert.get_subject().L = "London"
cert.get_subject().O = "Dummy Company Ltd"
cert.get_subject().OU = "Dummy Company Ltd"
cert.get_subject().CN = gethostname()
cert.set_serial_number(1000)
cert.gmtime_adj_notBefore(0)
cert.gmtime_adj_notAfter(10*365*24*60*60)
cert.set_issuer(cert.get_subject())
cert.set_pubkey(pubkey)
cert.sign(pubkey, signature)

print(cert, crypto.FILETYPE_PEM)

open(CERT_FILE, "wb").write(
	crypto.dump_certificate(crypto.FILETYPE_PEM, cert))
open(KEY_FILE, "wb").write(
	crypto.dump_privatekey(crypto.FILETYPE_PEM, pubkey))
