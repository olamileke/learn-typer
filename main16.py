from typing import Optional, List
import typer

app = typer.Typer()

@app.command()
def main(name: Optional[List[str]] = typer.Option(None)):
    if not name:
        raise typer.Abort()
    
    for n in name:
        typer.echo(n)

@app.command()
def numbers(number: Optional[List[float]] = typer.Option([])):
    typer.echo(f"The sum of the numbers is {sum(number)}")


@app.callback(invoke_without_command=True)
def callback():
    pass

if __name__ == '__main__':
    app()