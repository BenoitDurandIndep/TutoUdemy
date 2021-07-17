n1 = n2 =  ""

while not (n1.isdigit() and n2.isdigit()):
	n1 = input("Entrez un premier nombre : ")
	n2 = input("Entrez un deuxième nombre : ")
	if not (n1.isdigit() and n2.isdigit()):
		print("Veuillez entrer deux nombres valides")

print(f"Le résultat de l'addition du nombre {n1} avec le nombre {n2} est égal à {int(n1) + int(n2)}")
