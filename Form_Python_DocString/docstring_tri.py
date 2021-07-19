from pathlib import Path

rep_base=Path("D:/Formations/Python/a_trier")
rep_tri={".mp3":"Musique",
		".wav":"Musique",
		".flac":"Musique",
		".avi":"Videos",
		".mp4":"Videos",
		".gif":"Videos",
		".bmp":"Images",
		".png":"Images",
		".jpg":"Images",
		".txt":"Documents",
		".pptx":"Documents",
		".csv":"Documents",
		".xls":"Documents",
		".odp":"Documents",
		".pages":"Documents",
		".pdf":"Documents"
}
rep_cible=""

for f in rep_base.iterdir() :
	if f.is_file():
		rep_cible=rep_base / rep_tri.get(f.suffix,"Autres")
		rep_cible.mkdir(exist_ok=True)
		f.rename(rep_cible / f.name)

