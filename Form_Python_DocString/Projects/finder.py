from os import DirEntry
import pathlib
import typer
from typing import Optional
from pathlib import Path

app = typer.Typer()

@app.command('run')
def main(extension: str,
	directory: Optional[str] = typer.Argument(None, help="Dossier dans lequel chercher."),
	delete: bool = typer.Option(False, help="Supprime les fichiers trouvés.")):
	"""Affiche les fichiers trouvés pour l'extension sélectionnées, et les supprime selon l'option

	Args:
		extension (str): extesion des fichiers à chercher
		directory (Optional[str], optional): Répertoire où fairela recherche. Defaults to typer.Argumanet(None, help="Dossier dans lequel chercher.").
		delete (bool, optional): option pour supprimer les fichiers trouvés. Defaults to typer.Option(False, help="Supprime les fichiers trouvés.").
	"""
	mydir=Path.cwd()

	if directory:
		mydir=Path(directory)
	
	if not mydir.exists():
			typer.secho(f"Le dossier '{mydir}' n'exsite pas.", fg=typer.colors.RED)
			raise typer.Exit()

	files=mydir.rglob(f"*.{extension}")

	if delete:
		typer.confirm("Voulez-vous vraiment supprimer tous les fichiers trouvés ? ", abort=True)
		for f in files:
			f.unlink()
			typer.secho(f"Suppression du fichier {f}", fg=typer.colors.RED)
	else:
		typer.secho(f"Fichiers trouvés avec l'extension {extension}", fg=typer.colors.BLUE)
		for f in files:
			typer.echo(f)

@app.command()
def search(extension:str,
	directory: Optional[str] = typer.Argument(None, help="Dossier dans lequel chercher.")):
	"""Recherche les fichiers pour l'extension"""
	main(extension=extension, directory=directory, delete=False)
	

@app.command()
def delete(extension:str,
	directory: Optional[str] = typer.Argument(None, help="Dossier dans lequel chercher.")):
	"""Supprimer les fichiers pour l'extension"""
	main(extension=extension, directory=directory, delete=True)
	

if __name__=="__main__":
	app()