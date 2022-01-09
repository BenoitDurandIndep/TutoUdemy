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

	def remove_from_movie(self)->bool:
		list_movies=self._get_movies()
		if self.title in list_movies:
			list_movies.remove(self.title)
			self._write_movies(list_movies)
			return True
		else:
			logging.warning(f"The movie {self.title} is not in the list.")
			return False

	

def get_movies():
	with open(DATA_FILE,"r") as f:
		movies_title = json.load(f)

	movies=[Movie(movie_title) for movie_title in movies_title]
	return(movies)

if __name__=="__main__":
	m=Movie("harry potter")
	print(m.add_to_movies())
	print(m.remove_from_movie())
	print(m.add_to_movies())
	movies=get_movies()
	print(movies[0])

