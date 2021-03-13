# -*- coding: utf-8 -*-

from colorama import init as coloramaInit
from colorama import Fore, Style
from decimal import Decimal as dec
from genotype import STR_LOCUS_ALLELE_FREQUENCY_MAP as SLAFM
from individual import Parent, Child

coloramaInit()
RSLMR = RATE_OF_STR_LOCUS_MUTATION = 0.002
RSLPMMM = RATIO_OF_STR_LOCUS_PATERNAL_MUTATION_TO_MATERNAL_MUTATION = 3.5


class PaternityTest():
    def __init__(self, first_parent: Parent, second_parent: Parent, child: Child):
        self.child = child
        if first_parent.sex:
            self.father = first_parent
            self.mother = second_parent
        else:
            self.father = second_parent
            self.mother = first_parent

    @property
    def mutation_hypotheses(self):
        hypotheses = self.getHypotheses()
        return hypotheses

    # Whether that consistent with the law of gene segregation
    @staticmethod
    def ifSeparation(intersections):
        for i in intersections:
            if len(i) == 2:
                return True
        else:
            return False

    @staticmethod
    def ifNonParentage(intersections):
        for i in intersections:
            if len(i) != 0:
                return False
        else:
            return True

    @staticmethod
    def getProbability(hypothesis):
        step = hypothesis['step']
        if hypothesis['from'] == 1:
            ph = dec(0.5 * 0.5) * dec(RSLMR) * dec(10) ** dec(1-step) / dec(2)
        elif hypothesis['from'] == 0:
            ph = dec(0.5 * 0.5) * dec(RSLMR) * dec(10) ** dec(1-step) / dec(2) / dec(RSLPMMM)
        return ph

    def compare(self):
        zygotes = self.father.cross(self.mother)
        zygote_type = list(map(lambda z: z.type, zygotes))
        child_type = self.child.genotype.type
        intersections = list(map(lambda zt: set(child_type) & set(zt), zygote_type))
        if PaternityTest.ifSeparation(intersections):
            print(Fore.YELLOW + 'Genotypes consistent with the law of gene segregation' + Style.RESET_ALL)
            exit(1)
        if PaternityTest.ifNonParentage(intersections):
            print(Fore.YELLOW + 'Genotypes consistent with non parentage' + Style.RESET_ALL)
            exit(1)
        return zygotes, intersections

    def getHypotheses(self):
        hypotheses = []
        zygotes, intersections = self.compare()
        for zygote, intersection in list(zip(zygotes, intersections)):
            if len(intersection) == 1:
                stable = intersection.pop()
                #intersection.add(stable)
                for i, t in enumerate(zygote.type):
                    if t == stable:
                        from_parent = zygote.alleles[1-i].from_parent
                        original = zygote.type[1-i]
                        child_type = self.child.genotype.type
                        mutated = child_type[1-child_type.index(stable)]
                        loci = self.child.genotype.loci
                        typies = list(SLAFM[loci].keys())
                        step = abs(typies.index(original) - typies.index(mutated))
                        mutation_hypothesis = {
                            'step': step,
                            'from': from_parent,
                            'original': original,
                            'mutated': mutated
                        }
                        hypotheses.append(mutation_hypothesis)
        return hypotheses

    # Probability of Tested Individual is True Biological Parent(s)
    def GetX(self):
        hypotheses = self.getHypotheses()
        x = dec(0)
        for h in hypotheses: x += PaternityTest.getProbability(h)
        return x

    # Probability of Random Individual is True Biological Parent(s)
    def GetY(self):
        loci = self.child.genotype.loci
        type = self.child.genotype.type
        y = dec(2) * dec(SLAFM[loci][type[0]]) * dec(SLAFM[loci][type[1]])
        return y

    @staticmethod
    def getPaternityIndex(x, y):
        paternity_index = x / y
        return paternity_index
