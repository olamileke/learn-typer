import typer
import items
import users

app = typer.Typer(help="Awesome CLI Manager")

app.add_typer(users.app, name="users")
app.add_typer(items.app, name="items")

if __name__ == "__main__":
    app()