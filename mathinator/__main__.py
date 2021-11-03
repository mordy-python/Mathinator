#!/usr/bin/env python
import click, math
from . import utils


@click.group("Math")
def cli():
    """To use negative numbers, type -- then the negative number\n
    e.g ./math.py sqrt -- -9\n
    return 3.0i"""


@cli.command("qf")
@click.argument("a", type=float)
@click.argument("b", type=float)
@click.argument("c", type=float)
def quad_formula(a, b, c):
    inside = utils.under_house(a, b, c)
    under = 2 * a
    if b < 0:
        b = abs(b)
    else:
        b = -b
    formula_pt_1 = f"{b} ± √{inside}"
    tab_dist = f'{" "*int((len(formula_pt_1) / 2))}'
    formula = f'{formula_pt_1}\n{"-"*len(formula_pt_1)}\n{tab_dist}{under}'
    click.echo(formula)


@cli.command("sqrt")
@click.argument("num", type=float)
def sqrt_(num):
    if num < 0:
        sqrt = math.sqrt(abs(num))
        click.echo(f"{sqrt}i")
    else:
        click.echo(math.sqrt(num))


@cli.command("add")
@click.argument("a", type=float)
@click.argument("b", type=float)
def add(a, b):
    click.echo(utils.add(a, b))


@cli.command("sub")
@click.argument("a", type=float)
@click.argument("b", type=float)
def sub(a, b):
    click.echo(utils.sub(a, b))


@cli.command("mul")
@click.argument("a", type=float)
@click.argument("b", type=float)
def mul(a, b):
    click.echo(utils.mul(a, b))


@cli.command("div")
@click.argument("a", type=float)
@click.argument("b", type=float)
def div(a, b):
    click.echo(utils.div(a, b))


@cli.command("pow")
@click.argument("num", type=float)
@click.argument("pow", type=float)
def pow(num, pow):
    click.echo(num ** pow)


@cli.command("plus-minus")
@click.argument("a", type=float)
@click.argument("b", type=float)
@click.argument("c", type=float)
def plus_minus(a, b, c):
    a1 = a + b
    b1 = a - b
    a2 = f"{a1}"
    b2 = f"{b1}"
    result = f"{a2}\t{b2}"
    len_result_div_2 = int(len(result) / 2)
    click.echo(f'{result}\n{"-"*len(result)}\n{" "*len_result_div_2}{c}')


if __name__ == "__main__":
    cli()
