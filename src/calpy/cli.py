import click

from . import calculators


@click.command()
@click.option("--postfix", "notation", flag_value="postfix", default=True)
@click.option("--infix", "notation", flag_value="infix")
@click.argument("expression")
def main(notation, expression):
    try:
        result = getattr(calculators, notation)(expression)
    except Exception as e:
        raise click.ClickException(e)
    click.echo(result)


if __name__ == "__main__":
    main()
