from typing import List, Tuple
import typer

app = typer.Typer()

@app.command()
def command(names: List[str]):
    for name in names:
        typer.echo(name)

@app.command()
def olamileke(names: Tuple[str, str, str] = typer.Argument(("Fambegbe", "Olamileke", "Abiodun"))):
    fname, lname, zname = names
    typer.echo(zname)
    typer.echo(lname)
    typer.echo(fname)

@app.command()
def test():
    name = typer.prompt("What is your name")
    typer.echo(f"Hello {name}")

@app.command()
def check():
    confirm = typer.confirm("are you sure you want to delete ?")

    if confirm:
        typer.echo("Deleted")

    typer.echo("Happy you did not delete")

if __name__ == '__main__':
    app()