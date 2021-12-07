from typing import Optional
from datetime import datetime
import typer

app = typer.Typer()

@app.command()
def validate(id: int = typer.Argument(..., min=0 , max=100), age: int = typer.Option(20, min=18, clamp=True), score: float = typer.Option(0 , max=100, clamp=True)):
    typer.echo(f"ID is {id}")
    typer.echo(f"age is {age}")
    typer.echo(f"score is {score}")

@app.command()
def count(verbose: int = typer.Option(0, "--verbose", "-v", count=True)):
    typer.echo(f"Verbose count is {verbose}")

@app.command()
def hello(name: str, formal: Optional[bool] = typer.Option(None, "--accept/--reject")):
    if formal:
        typer.echo(f"Hello Mr {name}")
    else:
        typer.echo(f"Hello {name}")

@app.command()
def dob(dob: datetime):
    typer.echo(f"Interesting day to be born: {dob}")
    typer.echo(f"Interesting hour to be born: {dob.hour}")


if __name__ == "__main__":
    app()