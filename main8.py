import typer

def callback():
    pass

app = typer.Typer()

@app.command(help="Creating a user")
def create(name: str):
    typer.echo(f"Hello {name}")