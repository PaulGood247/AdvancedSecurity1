from Crypto.Cipher import DES
des = DES.new('12345678', DES.MODE_CBC, '0\0\0\0\0\0\0\0')
text = 'AAAABBBBAAAABBBB'
cipher_text = des.encrypt(text)

text1= 'AAC823F6BBE58F9EAF1FE0EB9CA7EB08'

b= []
for i in range(0, len(text1), 2):
     t=text1[i:i+2]
     b.append(int(t,16))
	 
final_text = bytes(b)
des.decrypt(final_text)
print(des.decrypt(final_text))

output1 = b'\x19\xffF7\xbb/\xe7|@E\xb6\xea\xd9D\xc1\xe3'
output2 = b'\xaa\xc8#\xf6\xbb\xe5\x8f\x9e\xaf\x1f\xe0\xeb\x9c\xa7\xeb\x08'