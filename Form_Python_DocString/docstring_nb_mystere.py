from random import randrange

nb_myst= randrange(1,101)
nb_essais_max=nb_essais=5
rep=""
encore= True

print("*** Le jeu du nombre mystère ***")

while encore :
	if nb_essais>0 :
		print(f"Il te reste {nb_essais} essais")
		rep = input("Devine le nombre : ")
		if rep.isdigit() : 
			if int(rep)==nb_myst : 
				print(f"""Bravo ! Le nombre mystère était bien {nb_myst} !
Tu as trouvé le nombre en {nb_essais_max-nb_essais} essais
Fin du jeu.""")
				encore=False
			elif int(rep)>nb_myst:
				print(f"Le nombre mystère est plus petit que {rep}")
				nb_essais-=1
			elif int(rep)<nb_myst:
				print(f"Le nombre mystère est plus grand que {rep}")
				nb_essais-=1
			else : 
				print("J'ai dû rater un truc ....")
		else : 
			print("Merci de saisir un nombre !")
	else:
		print(f"""Dommage : Le nombre mystère était {nb_myst}
Fin du jeu.""")
		encore=False
