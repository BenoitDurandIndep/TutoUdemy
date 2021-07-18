import json
from json.decoder import JSONDecodeError
import os 
from os import error

liste_courses=[]
choix = element = ""
encore =True
rep_save="D:/Formations/Python/TutoUdemy/Form_Python_DocString/data/"
fic_save = rep_save+"liste_courses.json"

try :
	with open(fic_save,'a+',encoding='utf-8') as f:
		f.seek(0)
		liste_courses = json.load(f)
except (IOError,JSONDecodeError) as e :
	print("Exception catchée : ",e)
	liste_courses=[]
	pass

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
			try :
				with open(fic_save,'w+',encoding='utf-8') as f:
					json.dump(liste_courses,f)
			except error as e:
				print(e)

			encore = False
			print("A bientôt !")
		else:
			print("Veillez saisir un chiffre entre 1 et 5 !")
	else : 
		print("Veillez saisir un chiffre entre 1 et 5 !")