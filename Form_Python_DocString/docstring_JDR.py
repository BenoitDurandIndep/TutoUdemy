from random import randrange

action =""
liste_actions=["1","2"]
pv_perso=pv_ennemi= pv_max=50
encore=action_demande=True
deg_perso=deg_ennemi=soin=0
nb_potions=3

while encore : 
	while action_demande and not action in liste_actions :
		action=input("Souhaitez-vous attaquez (1) ou utiliser une potion(2) ?")
	
	if action=="1" :
		deg_perso=randrange(5,11)
		
		pv_ennemi-=deg_perso

		print(f"Vous avez infligé {deg_perso} points de dégats à l'ennemi")
		if pv_ennemi<=0 : 
			print("Vous avez gangé ! ")
			encore=False
			break

	elif action =="2":
		if nb_potions>0 :
			soin = randrange(15,51)
			pv_perso+=soin
			nb_potions-=1
			action_demande=False
			if pv_perso>pv_max:
				pv_perso=pv_max
			
			print (f"La potion vous a soigné de {soin} points de vie, il vous reste {nb_potions} potions.")
			print (f"Vous avez maintenant {pv_perso} points de vie.")
		else:
			print("Il ne vous reste plus de potion !")
			continue

	deg_ennemi=randrange(5,16)
	pv_perso-=deg_ennemi
	print(f"L'ennemi vous a infligé {deg_ennemi} points de dégats")
	if pv_perso<=0 : 
		print("Vous avez perdu !")
		encore=False
		break
	else : 
		print(f"Il vous reste {pv_perso} points de vie.")
		print(f"Il reste {pv_ennemi} points de vie à l'ennemi.")
		print("-"*30)
		if not action=="2":
			action_demande=True
		action=""
