#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wx

from genotype import STR_LOCUS_ALLELE_FREQUENCY_MAP as SLAFM
from genotype import Allele, Genotype
from individual import Child, Parent
from paternitytest import PaternityTest
from wxbuild import WxFrame


class MPTK(WxFrame):

    def __init__(self, parent):
        super(MPTK, self).__init__(parent=parent)

        self.allele_choices_list = [self.fa_allele1, self.fa_allele2,
                                    self.ch_allele1, self.ch_allele2,
                                    self.mo_allele1, self.mo_allele2
        ]
        self.resetLocus()

    def resetLocus(self):
        loci_list = list(SLAFM.keys())
        self.locus.Clear()
        self.locus.SetItems(loci_list)

    def resetAlleles(self):
        loci_selection = self.locus.GetStringSelection()
        allele_list = [str(x) for x in list(SLAFM[loci_selection].keys())]
        for ac in self.allele_choices_list:
            ac.Clear()
            ac.SetItems(allele_list)

    @staticmethod
    def ifSeparation(intersections):
        if len(intersections) == 2:
            return True
        else:
            return False

    @staticmethod
    def ifNonParentage(intersections):
        if len(intersections) == 0:
            return True
        else:
            return False

    def GUICalculate(self):
        loci = self.locus.GetStringSelection()
        if self.fa_alleged.GetValue() and self.mo_alleged.GetValue():
            alleged = 'both'
        allele_selections = []
        for ac in self.allele_choices_list:
            selection = ac.GetStringSelection()
            if selection.isdigit():
                allele_selections.append(int(selection))
            else:
                allele_selections.append(float(selection))

        if alleged == 'both':
            af = Parent(Genotype(loci, Allele(allele_selections[0]),
                                 Allele(allele_selections[1])),
                                 sex=1, if_alleged=True)
            am = Parent(Genotype(loci, Allele(allele_selections[4]),
                                 Allele(allele_selections[5])),
                                 sex=0, if_alleged=True)
        ch = Child(Genotype(loci, Allele(allele_selections[2]),
                            Allele(allele_selections[3])))

        zygotes = af.cross(am)
        zygote_typies = list(map(lambda z: z.type, zygotes))
        child_type = ch.genotype.type
        intersections = list(map(lambda zt: set(child_type) & set(zt), zygote_typies))
        if PaternityTest.ifSeparation(zygote_typies, child_type):
            result_text = 'Genotypes consistent with the law of gene segregation.'
            return result_text
        if PaternityTest.ifNonParentage(intersections):
            result_text = 'Genotypes consistent with non parentage.'
            return result_text

        test = PaternityTest(af, am, ch)
        x = test.GetX()
        y = test.GetY()
        pi = test.getPaternityIndex(x, y)
        hypotheses = test.mutation_hypotheses

        result_text = '   Loci: {0}\n Father: {1}\n Mother: {2}\n  Child: {3}\nAlleged: {4}\n\nMutation Hypotheses:\n'.format(loci, str(af.genotype.type), str(am.genotype.type), str(ch.genotype.type), alleged)
        for h in hypotheses:
            p = test.getProbability(h)
            result_text += f'\tH: {str(h)}\n\tP = {float(p):.15f}\n'
        else:
            result_text += '\n'
        result_text += f' X = {x}\n Y = {y}\nPI = {pi}'
        return result_text

    def locusOnChoice(self, event):
        super(MPTK, self).locusOnChoice(event=event)
        self.resetAlleles()

    def calculateOnButtonClick(self, event):
        super(MPTK, self).calculateOnButtonClick(event=event)
        result_text = self.GUICalculate()
        self.result_strings.Clear()
        self.result_strings.SetValue(result_text)
        self.result_strings.SetInsertionPoint(-1)


if __name__ == '__main__':
    app = wx.App()
    frame = MPTK(None)
    frame.Show()
    app.MainLoop()