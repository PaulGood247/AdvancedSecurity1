def add(s, l):
	n= len(s)
	n1=l-n
	n2= n1-2
	s1=s
	for i in range(n2):
		s1+="\x00"
	
	n3 = str(n1)
	if len(n3) < 2: n3 = '0' + n3
	s1+= n3
	
	return(s1)

def decide_length(s):
	l = 1
	while (len(s) + l) % 16 != 0: l += 1
	return l + len(s)
	
def remove(s):
	sNoPadding = ""
	
	n= int(s[-2:])
	sNoPadding = s[:-n]
	
	return sNoPadding
	
from Crypto.Cipher import AES
aes = AES.new('1234567812345678', AES.MODE_ECB)
text = 'AAAABBBBCCCCDDDDAA'
text = add(text, decide_length(text))
cipher_text = aes.encrypt(text)
print(cipher_text)

text1='43D3215C92A75A1478FCF9CB950D20DB502A485FD5735486D57AEA9AA809E3DD'

b= []
for i in range(0, len(text1), 2):
     t=text1[i:i+2]
     b.append(int(t,16))
	 
final_text = bytes(b)
final_text = remove(aes.decrypt(final_text))
print(final_text)
