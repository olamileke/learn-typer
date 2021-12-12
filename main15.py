import typer


def latest_callback():
    """
        aoaoaoa
    """

app = typer.Typer()
users_app = typer.Typer(name="Olamileke", help="hahahah")
app.add_typer(users_app, callback=latest_callback, name="Segun", help="Damilare")

@users_app.callback("Abiodun", help="James")
def users():
    """
        Allows you to manage users in the app
    """

if __name__ == '__main__':
    app()