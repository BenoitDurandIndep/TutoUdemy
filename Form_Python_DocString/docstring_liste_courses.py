liste_courses=[]
choix = element = ""
encore =True

while encore : 
	print("""_______________________________
	Choisissez parmi les 5 options suivantes :
	1: Ajouter un élément à la liste
	2: Retirer un élément de la liste
	3: Afficher la liste
	4: Vider la liste
	5: Quitter""")

	choix= input(">> Votre choix : ")

	if choix.isdigit() and int(choix)>=1 and int(choix)<=5 : 
		if choix=="1" :
			element = input("Entrez le nom d'un élément à ajouter à la liste de courses : ")
			liste_courses.append(element)
			print(f"L'élément {element} a bien été ajouté à la liste.")
		elif choix=="2" :
			element = input("Entrez le nom d'un élément à retirer à la liste de courses : ")
			if element in liste_courses :
				liste_courses.remove(element)
				print(f"L'élément {element} a bien été supprimé de la liste.")
			else :
				print(f"L'élément {element} n'est pas présent dans la liste.")
		elif choix=="3" :
			if len(liste_courses)>0 :
				print("Voici le contenu de votre liste :")
				cpt=1
				for element in liste_courses :
					print(f"{cpt}. {element}")
					cpt+=1
			else:
				print("Votre liste ne contien aucun élément.")
		elif choix=="4":
			liste_courses.clear()
			print("La liste a été vidée de son contenu.")
		elif choix=="5":
			encore = False
			print("A bientôt !")
		else:
			print("Veillez saisir un chiffre entre 1 et 5 !")
	else : 
		print("Veillez saisir un chiffre entre 1 et 5 !")