from typing import List
import typer

valid_names = [("Fambegbe", "My surname"), ("Olamileke", "My first name"), ("Abiodun", "My middle name")]

def autocomplete(incomplete:str, ctx: typer.Context):
    names = ctx.params.get("name") or []
    for name, description in valid_names:
        if name.startswith(incomplete) and name not in names:
            yield((name, description))

def main(name: List[str] = typer.Option(["World"], "--name", help="The name to say hi to", autocompletion=autocomplete)):
    for each_name in name:
        typer.echo(f"Hello {each_name}")

if __name__ == '__main__':
    typer.run(main)