import struct
import base64
from Crypto.Hash import SHA256 

key = CryptoJS.SHA256('key').toString();

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
	while (len(s) + l) % 8 != 0: l += 1
	return l + len(s)

def message_blocks(m, n):
	#n = 2
	m=[m[i:i+n] for i in range(0, len(m), n)]
	return m


def xor_iterable(one, two):
	one, two = list(one), list(two)
	print(one, two)
	output = []
	for i in range(len(one)): output.append(one[i] ^ two[i])
	print(output)
	return bytes(output)

def davies_meyer(M, H):
	des = DES.new(H, DES.MODE_ECB)
	M= add(M, decide_length(M))
	print(M, H)
	cipher_text = des.encrypt(M)
	
	var concat = H + cipher_text;
	
	var MACKey = CryptoJS.HmacSHA256(concat, key);
	
	print("HMAC KEY : ", MACKey)
	print("Message: " ,cipher_text, len(cipher_text))
	#cipher_text = str(M).encode()
	print("Key: " ,H, len(H))
	i= xor_iterable(cipher_text, H)
	#a = struct.unpack("<2L", cipher_text)[0]
	#b = struct.unpack("<2L", H)[0]
	#print(a , b)
	#i= str(a ^ b)
	print(i , len(i))
	
	#b = str.encode(i)
	#print(b, len(b))
	return i
	#print(m1)
	#return cipher_text^H

from Crypto.Cipher import DES

m = 'AAAABBBBCCCCD'

m = add(m , decide_length(m))

iv = b'\0\0\0\0\0\0\0\0'
print(m, len(m))

m = message_blocks(m,2)

for val in m:
	print(val)
	iv =davies_meyer(val, iv)
	
print(base64.b16encode(iv))