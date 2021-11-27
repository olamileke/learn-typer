from typing import Optional
import typer

version = "1.0.0"

def version_callback(value: bool):
    if value:
        typer.echo(f"Awesome CLI version {version}")
        raise typer.Exit()

def name_callback(value: str):
    if value != "Olamileke":
        raise typer.BadParameter("Only Olamileke is allowed")

def main(name: str = typer.Option("aa", help="The name of the app", callback=name_callback), version: Optional[bool] = typer.Option(None, "--version", "-v", callback=version_callback, is_eager=True)):
    typer.echo("Hello World")

if __name__ == '__main__':
    typer.run(main)
