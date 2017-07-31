from PIL import Image

i= Image.open('pic.png')
j= Image.new('RGB', i.size)

w,h = i.size
m= "Bla Bla Bla"
m=''.join([bin(ord(x))[2:] for x in m])
print(m)
l = len(m)
size = w *h
print(size)
for q in range(size):
	m+=str(0)

k=0
for x in range(w):
	for y in range(h):
		p= i.getpixel((x,y))
		#j.putpixel((x,y), p)
		p = round(sum(p) / len(p))
		p = bin(p)[2:]
		p = p[:-1] + m[k]
		p = int(p, 2)
		#p1=bin(p[0])[2:]
		#p1=p1[:-1]+m[k]
		#p1=int(p1,2)
		tup=(p,p,p)
		#print(p,tup)
		k+=1
		j.putpixel((x,y), tup)
		
j.save('new_pic1.bmp')
j1 = Image.open('new_pic1.bmp')

k = 0
m2 = ''
for x in range(w):
	for y in range(h):
		p= j1.getpixel((x,y))
		#j.putpixel((x,y), p)
		p = round(sum(p) / len(p))
		m2 += bin(p)[-1]
print(m2[:l])