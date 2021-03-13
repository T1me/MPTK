# -*- coding: utf-8 -*-

import yaml

from colorama import init as coloramaInit
from colorama import Fore, Style

coloramaInit()
with open('frequency.yml', 'r') as f:
    SLAFM = STR_LOCUS_ALLELE_FREQUENCY_MAP = yaml.load(f, Loader=yaml.Loader)



class Allele():
    def __init__(self, allele_type, from_parent=None):
        self.type = allele_type
        self.from_parent = from_parent


class Genotype():
    '''Descript genotype of one loci.

    Args:
        loci (str): Which STR loci that current genotype belong to.
        first_allele: The first allele of this genotype as number.
        second_allele: The second allele of this genotype as number.

    Attributes:
        loci: The STR loci that current genotype belong to.
        type: A list include both two alleles.
    '''
    def __init__(self, loci: str, first_allele: Allele, second_allele: Allele):
        alleles = sorted([first_allele, second_allele], key=lambda x: x.type)
        self._loci = loci
        self._first_allele = alleles[0]
        self._second_allele = alleles[1]
        if not Genotype.ifLociLegal(self.loci):
            print(Fore.YELLOW + 'Illegal loci' + Style.RESET_ALL)
            exit(1)
        if not Genotype.ifTypeLegal(self.loci, self.type):
            print(Fore.YELLOW + 'Illegal genotype' + Style.RESET_ALL)
            exit(1)

    @property
    def loci(self) -> str:
        return self._loci

    @property
    def type(self) -> list:
        type = [self._first_allele.type, self._second_allele.type]
        return type

    @property
    def alleles(self) -> list:
        alleles = [self._first_allele, self._second_allele]
        return alleles

    @staticmethod
    def ifLociLegal(loci: str) -> bool:
        if loci in SLAFM:
            return True
        else:
            return False

    @staticmethod
    def ifTypeLegal(loci: str, type: list) -> bool:
        if type[0] in SLAFM[loci] and type[1] in SLAFM[loci]:
            return True
        else:
            return False
