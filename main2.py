from typing import Optional
import typer

def main(day:str, blue: Optional[bool] = None):
    if blue:
        text = typer.style(f"Today is {day}", fg=typer.colors.BLUE, bg=typer.colors.WHITE, bold=True, blink=True)
    else:
        text = typer.style(f"Today is {day}", fg=typer.colors.WHITE, bg=typer.colors.YELLOW)
    
    typer.echo(text, err=True)

if __name__ == '__main__':
    typer.run(main)