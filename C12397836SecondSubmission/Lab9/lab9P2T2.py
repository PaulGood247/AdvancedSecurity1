from OpenSSL import crypto, SSL
from socket import gethostname
from pprint import pprint
from time import gmtime, mktime

CERT_FILE = "selfsigned1.crt"
KEY_FILE = "private1.key"

def create_self_signed_cert():

	# create a key pair
	k = crypto.PKey()
	k.generate_key(crypto.TYPE_RSA, 1024)

	# create a self-signed cert

	message = 'Go left at the blue tree'
	with open('selfsigned.crt', "r") as my_cert_file:
		my_cert_text = my_cert_file.read()
		deviceCsr = crypto.load_certificate(crypto.FILETYPE_PEM, my_cert_text)

	#deviceCsr = crypto.load_certificate_request(crypto.FILETYPE_PEM, 'selfsigned.crt')
	with open('private.key', 'rb') as fh:
		CAprivatekey = crypto.load_privatekey(crypto.FILETYPE_PEM, fh.read())

		

	cert = crypto.X509()
	cert.set_serial_number(1000)
	cert.gmtime_adj_notBefore(0)
	cert.gmtime_adj_notAfter(10*365*24*60*60)
	cert.set_issuer(caCert.get_subject())
	cert.set_subject(deviceCsr.get_subject())
	cert.set_pubkey(deviceCsr.get_pubkey())
	cert.sign(CAprivatekey, digest)
	

create_self_signed_cert()