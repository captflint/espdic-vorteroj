
v = open('espdic.txt', 'r')
vortaro = v.read()

loko = 0

def venontaVico():
	global loko
	vico = ""
	vereco = False
	while vortaro[loko] != '\n':
		vico += vortaro[loko]
		if vortaro[loko] == ':':
			vereco = True
		loko += 1
	loko += 1
	if vereco:
		return(vico)
	else:
		return(venontaVico())

def tranĉi(vico):
	vorto = ""
	while vorto[-3:] != " : ":
		vorto += vico[0]
		vico = vico[1:]
	return((vorto[:-3], vico))

while True:
	t = tranĉi(venontaVico())
	print(t[0])
	print(t[1])
	input()
