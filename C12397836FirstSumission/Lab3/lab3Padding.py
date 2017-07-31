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

def remove(s):
	sNoPadding = ""
	
	n= int(s[-2:])
	sNoPadding = s[:-n]
	
	print(sNoPadding)