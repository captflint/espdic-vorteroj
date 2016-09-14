
v = open('espdic.txt', 'r')
vortaro = v.read()

f = open('vorteroj.txt', 'r')
finitaVortoj = f.read()
f.close()

vorteroj = open('vorteroj.txt', 'a')

loko = 0

def venontaVico():
	global loko
	if loko >= len(vortaro):
		print("FINFINE!! " * 1000)
		quit()
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

def erigi():
	vorto, difino = tranĉi(venontaVico())
	ruler = "    .    .    .    .    .    .    .    ."
	print('\n' + str(int(loko / len(vortaro) * 1000)))
	print(difino)
	print(ruler[:len(vorto)])
	print(vorto)
	respondo = input("> ")
	if respondo == '-':
		vorteroj.write(vorto)
	elif respondo == 'f':
		quit()
	else:
		numero = ''
		listoDeNumeroj = []
		for litero in respondo:
			if litero in '0123456789':
				numero += litero
			else:
				if len(numero) > 0:
					listoDeNumeroj.append(int(numero))
					numero = ''
		print(listoDeNumeroj)

while True:
	erigi()

