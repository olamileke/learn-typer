from typing import List
import typer

usernames: List[str] = ["Fambegbe", "Olamileke"]

def maybe_create_user(username:str):
    if username in usernames:
        typer.echo("The user already exists")
        raise typer.Exit(code=1)
    else:
        typer.echo(f"User created successfully: {username}")

def send_user_notification(username:str):
    typer.echo(f"Notification sent for user: {username}")

def main(username:str):
    maybe_create_user(username=username)
    send_user_notification(username=username)

if __name__ == '__main__':
    typer.run(main)