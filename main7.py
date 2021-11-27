from typing import Optional
import typer

def callback(verbose: bool = False):
    if verbose:
        typer.echo("Will write verbose outputss")
        state["verbose"] = True

app = typer.Typer(callback=callback)

state = {"verbose": False}

@app.command("create")
def cli_create_user(name: str):
    """
        Create a User
    """
    typer.echo(f"Creating user: {name}")

@app.command(help="This is the override module")
def delete(name: str, force: Optional[bool] = typer.Option(None, "--force", prompt="Are you sure you want to delete ?", help="Force option to know if to delete user or not")):
    """
        Delete a User
    """
    if force:
        typer.echo(f"Deleting user: {name}")
    else:
        typer.echo("Operation cancelled")

@app.callback()
def new_callback():
    typer.echo("Overriding the old callback")


if __name__ == '__main__':
    app()