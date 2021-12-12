from typing import Tuple
import typer

def main(user: Tuple[str, str, int] = typer.Option((None, None, None))):
    name, email, age = user

    typer.echo(name)
    typer.echo(email)
    typer.echo(age)

if __name__ == '__main__':
    typer.run(main);

