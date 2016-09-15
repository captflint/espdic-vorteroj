v = open('vorteroj.txt', 'r')

strikoj = 0

for litero in v.read():
	if litero == "'":
		strikoj += 1

print(strikoj)

