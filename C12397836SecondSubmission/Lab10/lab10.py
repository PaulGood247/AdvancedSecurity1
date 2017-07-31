from PIL import Image

i= Image.open('pic.png')
j= Image.new('RGB', i.size)

w,h = i.size

for x in range(w):
	for y in range(h):
		p= i.getpixel((x,y))
		j.putpixel((x,y), p)
		
j.save('new_pic.png')