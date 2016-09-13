
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
	if loko >= len(vortaro):
		print("FINFINE!!")
		quit()
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

def erigi():
	vorto, difino = tranĉi(venontaVico())
	ruler = "    .    .    .    .    .    .    .    ."
	print(int(loko / len(vortaro) * 100))
	print(difino)
	print(ruler[:len(vorto)])
	print(vorto)
	#respondo = input("> ")

while True:
	erigi()
