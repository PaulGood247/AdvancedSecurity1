def vigenere(message , key, encrypt=True):
	#message = "I shall exercise against you my right of rejection"
	#message = "YhwvtroiYudqPsebjatwptfoxgfzwjzqlbgioqcwelwlarblsgrmprochekewrvnsoyruvsndcljebvrkpkiumhybefsjrwutmvljgaybefldsydxmchfasxbojwlwfxxaphfjsbntzajukkwixithvbduyzkikwmeylpzsgdrdvwbuwmemmouolhtsajgwutmmmmzwxvlanebxejipktobndtzwnavqfnfxicgolhgsnsyxstuqfboxsfakdsipjnqjuvsuxnyzwjvgjskwusrpgoezqbklsgcrewtcdmwoafvlstgqqsfkielzamydaeeibgsnurgepvvlwipxfadogafuaojzfskruvssgpgoafrqiodiewsxitgldszukavlffoxsmgldsidsdvsuvsoadwjowerupqwjhwyctgldsgdxtcptcwxihwxqhlujbawpoqdxnygjsmhwyqgdogsdnlzamnlqlnmwspoitwjwbuptrglbddsay"
	
	#key = "password"
	
	print(ord('a'))
	print(ord('z'))
	message= message.replace(" ", "")
	
	for i in message:
		if ord(i.lower()) <97 or ord(i.lower())>122:
			message=message.replace(i, "")
	print(message)
	key=keyrepeat(key, len(message))
	one = []
	two = []
	three = []
	
	for i in message:
		one.append(ord(i.lower())-96)
	for i in key:
		two.append(ord(i.lower())-96)
		
	if encrypt is True :
		for index, i in enumerate(one):
			three.append(((one[index]+two[index])-1)%26)
	else:
		for index, i in enumerate(one):
			three.append(((one[index]-two[index])+1)%26)
	m = ""
	
	for i in three:
		if i == 0:
			i=26
		m += chr(i+96)
	print(m)
    
def keyrepeat(s, l):
    return (s * ((l/len(s))+1))[:l]
   
def encrypt(m, k):
    vigenere(m,k)
def decrypt(c,k):
	vigenere(c,k, False)