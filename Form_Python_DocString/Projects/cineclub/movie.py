import string
import json
import os
import logging

CUR_DIR  = os.path.dirname(__file__)
DATA_FILE=os.path.join(CUR_DIR,"data","movies.json")

class Movie:
	
	def __init__(self, title: str) ->None:
		self.title = title.title()

	#def __repr__(self):
	#	return self.title.title()

	def __str__(self):
		return self.title

	def _get_movies(self):
		try:
			with open(DATA_FILE,"r",encoding="utf-8") as f:
				return json.load(f)
		except FileNotFoundError as e:
			print(e)

	def _write_movies(self,movies):
		try:
			with open(DATA_FILE,"w+",encoding="utf-8") as f:
				json.dump(movies,f,indent=4)
		except FileNotFoundError as e:
			print(e)

	def add_to_movies(self)->bool:
		list_movies=self._get_movies()
		if self.title not in list_movies :
			list_movies.append(self.title)
			self._write_movies(list_movies)
			return True
		else:
			logging.warning(f"The movie {self.title} is already in the list.")
			return False

if __name__=="__main__":
	m=Movie("harry potter")
	print(m.add_to_movies())
	print(m)
