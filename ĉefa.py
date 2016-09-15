
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

def erigi(vorto, difino):
	ruler = "    .    .    .    .    .    .    .    ."
	neFinita = True
	while neFinita:
		print('\n' + str(int(loko / len(vortaro) * 1000)))
		print(difino)
		print(ruler[:len(vorto)])
		print(vorto)
		respondo = input("> ")
		erigitaVorto = vorto
		if respondo == '-':
			vorteroj.write(vorto + '\n')
			neFinita = False
		elif respondo in 'Ff':
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
			if len(numero) > 0:
				listoDeNumeroj.append(int(numero))
			if len(listoDeNumeroj) > 0:
				pasitaLiteroj = 0
				for numero in listoDeNumeroj:
					pasitaLiteroj += numero
					erigitaVorto = erigitaVorto[:pasitaLiteroj] + "'" + erigitaVorto[pasitaLiteroj:]
					pasitaLiteroj += 1
				print()
				print(difino)
				print(erigitaVorto)
				respondo2 = input("Ĉu ĉi tiu pravas? ")
				if respondo2 in 'jJ':
					vorteroj.write(erigitaVorto + '\n')
					neFinita = False

finitaListo = []
nuntempaVorto = ""
for litero in finitaVortoj:
	if litero == '\n':
		finitaListo.append(nuntempaVorto)
		nuntempaVorto = ""
	elif litero != "'":
		nuntempaVorto += litero

daŭriĝi = True
while daŭriĝi:
	vorto, difino = tranĉi(venontaVico())
	if vorto in finitaListo:
		pass
	else:
		erigi(vorto, difino)
		daŭriĝi = False

while True:
	vorto, difino = tranĉi(venontaVico())
	erigi(vorto, difino)

