import typer

app = typer.Typer()
items_app = typer.Typer()
users_app = typer.Typer()
app.add_typer(items_app, name="items")
app.add_typer(users_app, name="users")

@items_app.command("create")
def items_create(name: str):
    typer.secho(f"Creating item: {name}", bg=typer.colors.GREEN)

@items_app.command("delete")
def items_delete(name: str):
    typer.secho(f"Deleting item: {name}", bg=typer.colors.RED)

@users_app.command("create")
def users_create(name: str):
    typer.secho(f"Creating user: {name}", bg=typer.colors.GREEN)

@users_app.command("delete")
def users_delete(name: str):
    typer.secho(f"Deleting user: {name}", bg=typer.colors.RED)

if __name__ == '__main__':
    app()