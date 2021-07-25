from pathlib import Path

rep_base=Path("D:/Formations/Python/a_trier")
fic_source=rep_base / "prenoms.txt"
fic_cible=rep_base / "prenoms_clean.txt"

liste_finale=""
liste_prenoms=[]

prenoms_bruts=fic_source.read_text(encoding='UTF-8')
lignes_prenoms=prenoms_bruts.splitlines()
for l in lignes_prenoms:
	liste_prenoms.extend(l.split())

liste_prenoms=[p.strip("., ") for p in liste_prenoms]
# liste_prenoms.sort()

for p in sorted(liste_prenoms):
	liste_finale+=p+"\n"

fic_cible.write_text(liste_finale)
