import typer
import lands

app = typer.Typer()
app.add_typer(lands.app, name="lands")

@app.callback(invoke_without_command=True)
def callback():
    typer.echo("Heyaa. Awesome CLI manager here. Type --help to see more")

if __name__ == '__main__':
    app()