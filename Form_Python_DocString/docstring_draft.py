class Voiture :
	essence = 100

	def __init__(self,essence) :
		self.essence=essence

	def afficher_reservoir(self):
		print(f"La voiture contient {self.essence} litres d'essence")
	
	def roule(self,km):
		if self.essence<=0:
			print("Vous n'avez plus d'essence,faites le plein !")
			return
		self.essence-=(km*5)/100
		
		if self.essence<10:
			print("Vous n'avez bientôt plus d'essence !")

	def faire_le_plein(self,essence):
		self.essence+=essence

ma_voit=Voiture(50)

ma_voit.afficher_reservoir()
ma_voit.roule(25)
ma_voit.afficher_reservoir()
	

        

# nombres = [1, 21,5,44,4,9,5,83,29,31,25,38]
# nombres_pairs = [i for i in nombres if i%2 == 0]
# print(nombres_pairs)

# nombres = range(-10,10)
# nombres_positifs = [i for i in nombres if i>=0]
# print(nombres_positifs)

# nombres = range(5)
# nombres_doubles = [i*2 for i in nombres]
# print(nombres_doubles)

# nombres = range(10)
# nombres_inverses = [i*-1 for i in nombres if i%2 ]
# nombres_inverses.extend([i for i in nombres if i%2==0 ])
# print(sorted(nombres_inverses))

# import os

# fic=input("Entrez un fichier à ouvrir :")

# try:
# 	with open(fic,'r',encoding='utf-8') as f:
# 		print(f.read())
# except FileNotFoundError :
# 	print("Le fichier est introuvable.")
# except UnicodeError : 
# 	print("Le fichie ne peut pas être lu.")