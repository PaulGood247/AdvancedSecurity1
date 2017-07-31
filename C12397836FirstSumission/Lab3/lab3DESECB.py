from Crypto.Cipher import DES
des = DES.new('12345678', DES.MODE_ECB)
text = 'AAAABBBBAAAABBBB'
cipher_text = des.encrypt(text)
print(cipher_text)

text1= '19FF4637BB2FE77C19FF4637BB2FE77C'
for i in range(0, len(text1), 2):
     t=text1[i:i+2]
     b.append(int(t,16))
	 
final_text = bytes(b)
des.decrypt(final_text)

output = '\x19\xffF7\xbb/\xe7|\x19\xffF7\xbb/\xe7|'