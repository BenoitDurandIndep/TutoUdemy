from pathlib import Path

rep_base=Path("D:/Formations/Python/a_trier")
rep_cre={
	"Musique":["Rock","Pop","Electro","Classique"],
	"Films":["Actions","SF","Horreur"],
	"Séries":["Humour","Actions","Histoire"],
	"Divers":[]
}
rep_cible=ss_rep_cible=""

for rep,liste_rep in rep_cre.items():
	for ss_rep in liste_rep:
		ss_rep_cible= rep_base / rep /ss_rep
		ss_rep_cible.mkdir(exist_ok=True, parents=True)

