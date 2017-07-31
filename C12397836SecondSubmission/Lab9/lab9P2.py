def main():
	cert = crypto.X509()
	cert.set_serial_number(serial_no)
	cert.gmtime_adj_notBefore(notBeforeVal)
	cert.gmtime_adj_notAfter(notAfterVal)
	cert.set_issuer(caCert.get_subject())
	cert.set_subject(deviceCsr.get_subject())
	cert.set_pubkey(deviceCsr.get_pubkey())
	cert.sign(CAprivatekey, digest)
	print(cert)
	return cert