mdp = input("Entrez un mot de passe (min 8 caractères) : ")
mdp_trop_court = "votre mot de passe est trop court."
mdp_que_nombre="Votre mot de passe ne contient que des nombres."
mdp_ok="Inscription terminée."

if len(mdp) == 0 :
	print(mdp_trop_court.upper())
elif len(mdp) < 8 :
	print(mdp_trop_court.capitalize())
elif mdp.isdigit() :
	print(mdp_que_nombre)
else :
	print(mdp_ok)