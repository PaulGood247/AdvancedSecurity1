#from RandomnessTests import RandomnessTester

m = 11*19
xi = 9

def rng():
	global xi
	xi = (xi*xi)%m
	return xi

bitstr = ""
for i in range(120):
	bitstr += bin(rng())[-1:]
	
#rng_tester = RandomnessTester(None)
#p_value = rng_tester.monobit(bitstr)
print(int(bitstr, 4))
