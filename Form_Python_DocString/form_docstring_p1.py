n1 = input("Entrez un premier nombre : ")
n2 = input("Entrez un deuxième nombre : ")
rep=""

if(n1.isdigit() and n2.isdigit()):
	res = int(n1) + int(n2)
	rep=f"Le résultat de l'addition du nombre {n1} avec le nombre {n2} est égal à {res}"
else : 
	rep="Il faut saisir des entiers !"

print(rep)