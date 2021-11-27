import typer

valid_names = [("Fambegbe", "My surname"), ("Olamileke", "My first name"), ("Abiodun", "My middle name"), ("Olamide", "Some random name")]

def complete_name(incomplete: str):
    for name, description in valid_names:
        if name.startswith(incomplete):
            yield((name, description))
    
def main(name:str = typer.Option(..., "--name", "-n", help="The name to say hi to.", autocompletion=complete_name)):
    typer.echo(f"My name is {name}")

if __name__ == "__main__":
    typer.run(main)