import click
from .chat import chat


@click.group()
@click.pass_context
def cli(ctx):
    ctx.ensure_object(dict)


@cli.command()
@click.pass_context
@click.argument('message')
def chatgpt(ctx, message):
    click.echo('start sub')
    click.echo(">" + message)
    print(chat(message))


if __name__ == '__main__':
    cli(obj={})
