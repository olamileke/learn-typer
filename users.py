import typer 

app = typer.Typer()

@app.command()
def create(name: str):
    typer.echo(f"Creating user: {name}")

@app.command()
def delete(name: str):
    typer.echo(f"Deleting user: {name}")

if __name__ == "__main__":
    app()