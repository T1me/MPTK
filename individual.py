# -*- coding: utf-8 -*-

from colorama import init as coloramaInit
from colorama import Fore, Style
from genotype import Allele, Genotype

coloramaInit()


class Individual():
    def __init__(self, genotype: Genotype, sex: bool = None):
        self._genotype = genotype
        self._sex=sex

    @property
    def genotype(self):
        return self._genotype

    @property
    def sex(self) -> bool:
        return self._sex


class Parent(Individual):
    '''Parent in paternity test.

    Args:
        genotype (Genotype): Genotype.
        sex (bool): Biological sexes. 1 as male, 0 as female.
        if_alleged (bool): 1 as alleged, 0 as not alleged.

    Attributes:
        genotype: Genotype.
        sex: Biological sexes. 1 as male, 0 as female.
        if_alleged: 1 as alleged, 0 as not alleged.
    '''
    def __init__(self, genotype: Genotype, sex: bool = None, if_alleged: bool = True):
        super().__init__(genotype, sex)
        self._if_alleged = if_alleged

    @property
    def ifAlleged(self) -> bool:
        return self._if_alleged

    def ifParentsDiffSexes(self, another_parent) -> bool:
        if self.sex != another_parent.sex:
            return True
        else:
            return False

    def ifParentsSameLoci(self, another_parent) -> bool:
        if self.genotype.loci == another_parent.genotype.loci:
            return True
        else:
            return False

    def cross(self, another_parent) -> list:
        if not self.ifParentsDiffSexes(another_parent):
            print(Fore.YELLOW + 'Parents have the same sex' + Style.RESET_ALL)
            exit(1)
        if not self.ifParentsSameLoci(another_parent):
            print(Fore.YELLOW + 'Parents have different locus' + Style.RESET_ALL)
            exit(1)
        zygotes=[]
        for allele in self.genotype.alleles:
            for another_allele in another_parent.genotype.alleles:
                zygote_genotype = Genotype(loci=self.genotype.loci,
                                  first_allele=Allele(allele_type=allele.type,
                                                      from_parent=self.sex),
                                  second_allele=Allele(allele_type=another_allele.type,
                                                       from_parent=another_parent.sex))
                zygotes.append(zygote_genotype)
        return zygotes


class Child(Individual):
    '''Parent in paternity test.

    Args:
        genotype (Genotype): Genotype.

    Attributes:
        genotype: Genotype.
    '''
    pass
