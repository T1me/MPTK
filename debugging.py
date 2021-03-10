#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from genotype import Genotype, Allele
from individual import Parent, Child
from paternitytest import PaternityTest

af = Parent(Genotype('vWA', Allele(14), Allele(18)), sex=1, if_alleged=True)
am = Parent(Genotype('vWA', Allele(18), Allele(18)), sex=0, if_alleged=True)
ch = Child(Genotype('vWA', Allele(18), Allele(19)))

test = PaternityTest(af, am, ch)
hypotheses = test.mutation_hypotheses
x = test.GetX()
y = test.GetY()
pi = test.getPaternityIndex(x, y)
print('Mutation Hypotheses:')
for h in hypotheses: print('\t' + str(h))
print('X = ' + str(x))
print('Y = ' + str(y))
print('PI = ' + str(pi))