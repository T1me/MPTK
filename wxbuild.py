# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class WxFrame
###########################################################################

class WxFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"MPTK", pos = wx.DefaultPosition, size = wx.Size( 550,650 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.FRAME_SHAPED|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		main = wx.BoxSizer( wx.VERTICAL )

		loci_text = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"STR 基因座" ), wx.VERTICAL )

		STR_loci = wx.GridSizer( 0, 0, 0, 0 )

		locusChoices = []
		self.locus = wx.Choice( loci_text.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), locusChoices, 0 )
		self.locus.SetSelection( 0 )
		STR_loci.Add( self.locus, 0, wx.BOTTOM|wx.LEFT, 5 )


		loci_text.Add( STR_loci, 1, wx.EXPAND, 5 )


		main.Add( loci_text, 0, wx.TOP|wx.BOTTOM|wx.EXPAND, 5 )

		genotype_text = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"基因分型" ), wx.VERTICAL )

		genotype = wx.GridSizer( 0, 3, 0, 0 )

		fa = wx.StaticBoxSizer( wx.StaticBox( genotype_text.GetStaticBox(), wx.ID_ANY, u"父亲" ), wx.VERTICAL )

		fa_alleles = wx.GridSizer( 0, 2, 0, 0 )

		self.fa_allele1_text = wx.StaticText( fa.GetStaticBox(), wx.ID_ANY, u"第一等位基因", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.fa_allele1_text.Wrap( -1 )

		fa_alleles.Add( self.fa_allele1_text, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		fa_allele1Choices = []
		self.fa_allele1 = wx.Choice( fa.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, fa_allele1Choices, 0 )
		self.fa_allele1.SetSelection( 0 )
		self.fa_allele1.SetMaxSize( wx.Size( 50,-1 ) )

		fa_alleles.Add( self.fa_allele1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.fa_allele2_text = wx.StaticText( fa.GetStaticBox(), wx.ID_ANY, u"第二等位基因", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.fa_allele2_text.Wrap( -1 )

		fa_alleles.Add( self.fa_allele2_text, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		fa_allele2Choices = []
		self.fa_allele2 = wx.Choice( fa.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, fa_allele2Choices, 0 )
		self.fa_allele2.SetSelection( 0 )
		self.fa_allele2.SetMaxSize( wx.Size( 50,-1 ) )

		fa_alleles.Add( self.fa_allele2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fa_alleged = wx.CheckBox( fa.GetStaticBox(), wx.ID_ANY, u"疑似父亲", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.fa_alleged.SetValue(True)
		self.fa_alleged.Enable( False )

		fa_alleles.Add( self.fa_alleged, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		fa.Add( fa_alleles, 0, wx.EXPAND, 5 )


		genotype.Add( fa, 1, wx.EXPAND|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )

		ch = wx.StaticBoxSizer( wx.StaticBox( genotype_text.GetStaticBox(), wx.ID_ANY, u"孩子" ), wx.VERTICAL )

		ch_alleles = wx.GridSizer( 0, 2, 0, 0 )

		self.ch_allele1_text = wx.StaticText( ch.GetStaticBox(), wx.ID_ANY, u"第一等位基因", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ch_allele1_text.Wrap( -1 )

		ch_alleles.Add( self.ch_allele1_text, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		ch_allele1Choices = []
		self.ch_allele1 = wx.Choice( ch.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, ch_allele1Choices, 0 )
		self.ch_allele1.SetSelection( 0 )
		self.ch_allele1.SetMaxSize( wx.Size( 50,-1 ) )

		ch_alleles.Add( self.ch_allele1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.ch_allele2_text = wx.StaticText( ch.GetStaticBox(), wx.ID_ANY, u"第二等位基因", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ch_allele2_text.Wrap( -1 )

		ch_alleles.Add( self.ch_allele2_text, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		ch_allele2Choices = []
		self.ch_allele2 = wx.Choice( ch.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, ch_allele2Choices, 0 )
		self.ch_allele2.SetSelection( 0 )
		self.ch_allele2.SetMaxSize( wx.Size( 50,-1 ) )

		ch_alleles.Add( self.ch_allele2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		ch_alleles.Add( ( 0, 0), 1, wx.ALL, 5 )


		ch.Add( ch_alleles, 0, wx.EXPAND, 5 )


		genotype.Add( ch, 1, wx.EXPAND|wx.TOP|wx.BOTTOM, 5 )

		mo = wx.StaticBoxSizer( wx.StaticBox( genotype_text.GetStaticBox(), wx.ID_ANY, u"母亲" ), wx.VERTICAL )

		mo_alleles = wx.GridSizer( 0, 2, 0, 0 )

		self.mo_allele1_text = wx.StaticText( mo.GetStaticBox(), wx.ID_ANY, u"第一等位基因", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.mo_allele1_text.Wrap( -1 )

		mo_alleles.Add( self.mo_allele1_text, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		mo_allele1Choices = []
		self.mo_allele1 = wx.Choice( mo.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, mo_allele1Choices, 0 )
		self.mo_allele1.SetSelection( 0 )
		self.mo_allele1.SetMaxSize( wx.Size( 50,-1 ) )

		mo_alleles.Add( self.mo_allele1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.mo_allele2_text = wx.StaticText( mo.GetStaticBox(), wx.ID_ANY, u"第二等位基因", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.mo_allele2_text.Wrap( -1 )

		mo_alleles.Add( self.mo_allele2_text, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		mo_allele2Choices = []
		self.mo_allele2 = wx.Choice( mo.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, mo_allele2Choices, 0 )
		self.mo_allele2.SetSelection( 0 )
		self.mo_allele2.SetMaxSize( wx.Size( 50,-1 ) )

		mo_alleles.Add( self.mo_allele2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.mo_alleged = wx.CheckBox( mo.GetStaticBox(), wx.ID_ANY, u"疑似母亲", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.mo_alleged.SetValue(True)
		self.mo_alleged.Enable( False )

		mo_alleles.Add( self.mo_alleged, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		mo.Add( mo_alleles, 0, wx.EXPAND, 5 )


		genotype.Add( mo, 1, wx.EXPAND|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )


		genotype_text.Add( genotype, 1, wx.EXPAND, 5 )


		main.Add( genotype_text, 0, wx.TOP|wx.BOTTOM|wx.EXPAND, 5 )

		result_text = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"结果" ), wx.VERTICAL )

		result = wx.BoxSizer( wx.VERTICAL )

		self.result_strings = wx.TextCtrl( result_text.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		self.result_strings.SetFont( wx.Font( 10, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas" ) )

		result.Add( self.result_strings, 1, wx.EXPAND|wx.TOP|wx.BOTTOM, 5 )


		result_text.Add( result, 1, wx.EXPAND, 5 )


		main.Add( result_text, 1, wx.BOTTOM|wx.EXPAND|wx.TOP, 5 )

		self.calculate = wx.Button( self, wx.ID_ANY, u"计算", wx.DefaultPosition, wx.DefaultSize, 0 )
		main.Add( self.calculate, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )


		self.SetSizer( main )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.locus.Bind( wx.EVT_CHOICE, self.locusOnChoice )
		self.calculate.Bind( wx.EVT_BUTTON, self.calculateOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def locusOnChoice( self, event ):
		event.Skip()

	def calculateOnButtonClick( self, event ):
		event.Skip()


