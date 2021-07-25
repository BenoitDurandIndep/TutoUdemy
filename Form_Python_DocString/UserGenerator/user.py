import faker
import logging
from pathlib import Path

BASE_DIR=Path(__file__).resolve().parent

logging.basicConfig(level=logging.DEBUG,
filename=BASE_DIR/"user_generator.log"
)

fake = faker.Faker()

def get_user() ->str :
	"""Generates the firstname and name of a user

	Returns:
		str: the generated name
	"""
	logging.debug("Generating a user")
	return fake.unique.name()
	

def get_users(nb :int =1) ->list[str]:
	"""Generates a list of nb users

	Args:
		nb (int, optional): Number of generated users. Defaults to 1.

	Returns:
		list[str]: The list of the users
	"""
	logging.info(f"Generating a {nb} users")
	return [get_user() for i in range(nb)]

if __name__=="__main__":
	user=get_users(nb=5)
	print(user)
