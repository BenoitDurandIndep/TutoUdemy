import logging
from pathlib import Path
import json

from  constants import DATA_DIR,CUR_DIR

logging.basicConfig(level=logging.INFO,
filename=Path(CUR_DIR) / "user_generator.log"
)

LOGGER=logging.getLogger()

class Liste(list):
	def __init__(self,nom):
		self.nom=nom

	def ajouter(self, element :str) ->bool:
		if not isinstance(element, str):
			raise ValueError("Vous ne pouvez ajouter que des chaines de caractères!")
		
		if element in self:
			LOGGER.error(f"{element} est déjà dans la liste.")
			return False
		
		self.append(element)
		return True
	
	def enlever(self,element :str) ->bool:
		if element in self:
			self.remove(element)
			return True
		return False

	def affichier(self):
		print(f"Ma liste de {self.nom}")
		for e in self:
			print(f" - {e}")

	def sauvegarder(self) ->bool:
		chemin = DATA_DIR / (self.nom+".json")
		chemin.mkdir(exist_ok=True, parents=True)

		with open(chemin,"w",encoding='utf-8') as f:
			json.dump(self,f)
		
		return True

if __name__=="__main__":
	ma_liste=Liste("Courses")
	res=ma_liste.ajouter("Pommes")
