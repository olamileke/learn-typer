import typer

app = typer.Typer()

@app.command(context_settings={"allow_extra_args": True, "ignore_unknown_options": True})
def main(name: str, ctx: typer.Context):
    typer.echo(name)
    for args in ctx.args:
        typer.echo(f"Extra CLI argument: {args}")

if __name__ == "__main__":
    app()