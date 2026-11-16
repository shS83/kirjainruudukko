taso = int(input("Kerrokset: "))
no = taso * 2 - 1
ruudukko = [[" " for y in range(no)] for x in range(no)]

cx = len(ruudukko) // 2
cy = len(ruudukko) // 2
ruudukko[cx][cy] = "A"

for add in range(taso-1, 0, -1):
	for y in range(-add, add+1):
		for x in range(-add, add+1):
			if x == 0 and y == 0:
				continue
			ruudukko[cx+x][cy+y] = chr(65 + add)

for rivi in ruudukko:
	for sarake in rivi:
		print(sarake, end="")
	print()