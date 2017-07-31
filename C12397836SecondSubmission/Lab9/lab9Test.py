
def signRequestObject(self,
                          issuerDistinguishedName,
                          requestObject,
                          serialNumber,
                          secondsToExpiry=60 * 60 * 24 * 365, # One year
                          digestAlgorithm='md5'):
        """
        Sign a CertificateRequest instance, returning a Certificate instance.
        """
        req = requestObject.original
        dn = requestObject.getSubject()
        cert = crypto.X509()
        issuerDistinguishedName._copyInto(cert.get_issuer())
        cert.set_subject(req.get_subject())
        cert.set_pubkey(req.get_pubkey())
        cert.gmtime_adj_notBefore(0)
        cert.gmtime_adj_notAfter(secondsToExpiry)
        cert.set_serial_number(serialNumber)
        cert.sign(self.original, digestAlgorithm)
        return Certificate(cert)
		
