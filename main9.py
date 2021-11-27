import typer

app = typer.Typer()

@app.command()
def create(name: str): 
    typer.echo(f"Creating user: {name}")


@app.command()
def delete(name: str): 
    typer.echo(f"Deletijng user: {name}")

@app.callback()
def callback(ctx: typer.Context):
    typer.echo(f"Executing command: {ctx.invoked_subcommand}")