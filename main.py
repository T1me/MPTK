#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import click
from genotype import Allele, Genotype
from genotype import STR_LOCUS_ALLELE_FREQUENCY_MAP as SLAFM
from individual import Parent, Child
from paternitytest import PaternityTest


@click.command()
@click.option('-l', '--loci', nargs=1, required=True,
              help='STR loci.               ', metavar='<loci>',
              type=click.Choice(list(SLAFM.keys()), case_sensitive=False))
@click.option('-f', '--father', nargs=2, required=True,
              help='Genotype of the father. ',
              type=(int, int), metavar='<alleles>')
@click.option('-m', '--mother', nargs=2, required=True,
              help='Genotype of the mother. ',
              type=(int, int), metavar='<alleles>')
@click.option('-c', '--child', nargs=2, required=True,
              help='Genotype of the child.  ',
              type=(int, int), metavar='<alleles>')
@click.option('-a', '--alleged', nargs=1, default='both',
              help='The alleged individual. (default "both")',
              type=click.Choice(['both']))
@click.option('-q', '--quiet', help='Running in quiet mode.', flag_value=True)
def calculate(loci, father, mother, child, alleged, quiet):
    if alleged == 'both':
        af = Parent(Genotype(loci, Allele(father[0]), Allele(father[1])),
                             sex=1, if_alleged=True)
        am = Parent(Genotype(loci, Allele(mother[0]), Allele(mother[1])),
                             sex=0, if_alleged=True)
    ch = Child(Genotype(loci, Allele(child[0]), Allele(child[1])))

    test = PaternityTest(af, am, ch)
    x = test.GetX()
    y = test.GetY()
    pi = test.getPaternityIndex(x, y)

    if not quiet:
        click.echo('   Loci: ' + loci)
        click.echo(' Father: ' + str(father))
        click.echo(' Mother: ' + str(mother))
        click.echo('  Child: ' + str(child))
        click.echo('Alleged: ' + alleged)
        click.echo()
        hypotheses = test.mutation_hypotheses
        click.echo('Mutation Hypotheses:')
        for h in hypotheses:
            p = test.getProbability(h)
            click.echo(f'\t{str(h)}\tP = {float(p):.15f}')
        click.echo(' X = ' + str(x))
        click.echo(' Y = ' + str(y))
    click.echo('PI = ' + str(pi))


if __name__ == '__main__':
    calculate()