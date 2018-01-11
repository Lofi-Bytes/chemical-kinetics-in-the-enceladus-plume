# -*- coding: utf-8 -*-

#***********************************************************************
# Importing everything python needs in order to be smart.
#***********************************************************************
import numpy as np                                      			# Numpy tells python how to do array operations.
import rates
reload(rates)
from rates import *
from mapper import *

#***********************************************************************
# Calculate the sources and losses for each neutral species.
#***********************************************************************
def f(n, t):
	
	S = np.zeros(n.shape)
	L = np.zeros(n.shape)
	
	#******************************** H2O **********************************
	S[mapper['H2O']] = ((K13)*n[mapper['H2O+']]) * n[mapper['H2O']]

	L[mapper['H2O']] = ((J04 + J05 + J10 + J11 + J12 + J13) \
					 + (D02 + I04 + ID01 + ID02 + ID03)*n[mapper['e']] \
					 + (D05 + I09 + ID04 + ID05 + ID06)*n[mapper['eh']] \
					 + (K04)*n[mapper['H+']] \
					 + (K08)*n[mapper['O+']] \
					 + (K10 + K11)*n[mapper['OH+']] \
					 + (K12 + K13)*n[mapper['H2O+']] \
					 + (K19 + K20)*n[mapper['H2+']]) * n[mapper['H2O']]

	#******************************** OH ***********************************
	S[mapper['OH']] 	= ((J04 + J11 + D02) \
				+ (ID01)*n[mapper['e']] \
				+ (D05 + ID04)*n[mapper['eh']] \
				+ (K11)*n[mapper['OH+']] \
				+ (K12)*n[mapper['H2O+']]) * n[mapper['H2O']] \
				+ ((RD02)*n[mapper['e']] \
				+ (RD07)*n[mapper['eh']]) * n[mapper['H2O+']] \
				+ ((RD03)*n[mapper['e']] \
				+ (RD08)*n[mapper['eh']]) * n[mapper['H3O+']]

	L[mapper['OH']] 	= ((J02 + J03) \
				+ (D01 + I01)*n[mapper['e']] \
				+ (D04 + I08)*n[mapper['eh']] \
				+ (K03)*n[mapper['H+']] \
				+ (K07)*n[mapper['O+']] \
				+ (K09)*n[mapper['OH+']] \
				+ (K17 + K18)*n[mapper['H2+']]) * n[mapper['OH']]

	#******************************** H ************************************
	S[mapper['H']] 		= ((J04 + J13 + D02) \
				+ (2*ID02 + ID03)*n[mapper['e']] \
				+ (D05 + ID05 + 2*ID06)*n[mapper['eh']]) * n[mapper['H2O']] \
				+ ((J03 + D01) \
				+ (D04)*n[mapper['eh']]) * n[mapper['OH']] \
				+ ((J08 + J09 + 2*D03) \
				+ 2*(D06)*n[mapper['eh']] \
				+ (K21)*n[mapper['O+']] \
				+ (K24)*n[mapper['OH+']] \
				+ (K25)*n[mapper['H2O+']]) * n[mapper['H2']] \
				+ ((R01)*n[mapper['e']] \
				+ (R04)*n[mapper['eh']] \
				+ (K01)*n[mapper['H']] \
				+ (K02)*n[mapper['O']] \
				+ (K03)*n[mapper['OH']] \
				+ (K04)*n[mapper['H2O']] \
				+ (K14)*n[mapper['H2']]) * n[mapper['H+']] \
				+ ((RD01)*n[mapper['e']] \
				+ (RD06)*n[mapper['eh']]) * n[mapper['OH+']] \
				+ ((RD02)*n[mapper['e']] \
				+ (RD07)*n[mapper['eh']]) * n[mapper['H2O+']] \
				+ ((2*RD04)*n[mapper['e']] \
				+ 2*(RD05)*n[mapper['eh']] \
				+ (K16)*n[mapper['O']] \
				+ (K17)*n[mapper['OH']] \
				+ (K19)*n[mapper['H2O']]) * n[mapper['H2+']]

	L[mapper['H']] 		= ((J06) \
				+ (I02)*n[mapper['e']]  \
				+ (I06)*n[mapper['eh']] \
				+ (K01)*n[mapper['H+']] \
				+ (K05)*n[mapper['O+']]) * n[mapper['H']]

	#******************************** H2 ***********************************
	S[mapper['H2']] 	= (J05 + J12)*n[mapper['H2O']] \
				+ ((RD03)*n[mapper['e']] \
				+ (RD08)*n[mapper['eh']]) * n[mapper['H3O+']] \
				+ ((K15)*n[mapper['H2']] \
				+ (K18)*n[mapper['OH']] \
				+ (K20)*n[mapper['H2O']]) * n[mapper['H2+']]

	L[mapper['H2']] 	= ((J07 + J08 + J09) \
				+ (D03)*n[mapper['e']] \
				+ (D06)*n[mapper['eh']] \
				+ (K14)*n[mapper['H+']] \
				+ (K15)*n[mapper['H2+']] \
				+ (K21)*n[mapper['O+']] \
				+ (K24)*n[mapper['OH+']] \
				+ (K25)*n[mapper['H2O+']]) * n[mapper['H2']]

	#******************************** O ************************************
	S[mapper['O']] 		= (J05) * n[mapper['H2O']] \
				+ ((J03 + D01) \
				+ (D04)*n[mapper['eh']] \
				+ (K23)*n[mapper['O']]) * n[mapper['OH']] \
				+ ((R02)*n[mapper['e']] \
				+ (R05)*n[mapper['eh']] \
				+ (K05)*n[mapper['H']] \
				+ (K06)*n[mapper['O']] \
				+ (K07)*n[mapper['OH']] \
				+ (K08)*n[mapper['H2O']]) * n[mapper['O+']] \
				+ ((RD01)*n[mapper['e']] \
				+ (RD06)*n[mapper['eh']] \
				+ (K09)*n[mapper['OH']] \
				+ (K10)*n[mapper['H2O']]) * n[mapper['OH+']]

	L[mapper['O']] 		= ((J01) \
				+ (I03)*n[mapper['e']] \
				+ (I07)*n[mapper['eh']] \
				+ (K02)*n[mapper['H+']] \
				+ (K06)*n[mapper['O+']] \
				+ (K16)*n[mapper['H2']] \
				+ (K22 + K23)*n[mapper['OH']]) * n[mapper['O']]

	#***********************************************************************
	# Calculate the sources and losses for each ion species.
	#***********************************************************************

	#******************************** H2O+ *********************************
	S[mapper['H2O+']] 	= ((J10) \
				+ (I04)*n[mapper['e']] \
				+ (I09)*n[mapper['eh']] \
				+ (K04)*n[mapper['H+']] \
				+ (K08)*n[mapper['O+']] \
				+ (K11)*n[mapper['OH+']] \
				+ (K13)*n[mapper['H2O+']] \
				+ (K20)*n[mapper['H2+']]) * n[mapper['H2O']] \
				+ ((K09)*n[mapper['OH+']] \
				+ (K17)*n[mapper['H2+']]) * n[mapper['OH']] \
				+ ((K24)*n[mapper['OH+']]) * n[mapper['H2']] 

	L[mapper['H2O+']] 	= ((RD02)*n[mapper['e']] \
				+ (RD07)*n[mapper['eh']] \
				+ (K12 + K13)*n[mapper['H2O']] \
				+ (K25)*n[mapper['H2']]) * n[mapper['H2O+']]

	#******************************** H3O+ *********************************
	S[mapper['H3O+']] 	= ((K10)*n[mapper['OH+']] \
				+ (K12)*n[mapper['H2O+']] \
				+ (K19)*n[mapper['H2+']] ) * n[mapper['H2O']] \
				+ ((K25)*n[mapper['H2O+']]) * n[mapper['H2']] 

	L[mapper['H3O+']] 	= ((RD03)*n[mapper['e']] 
				+ (RD08)*n[mapper['eh']]) * n[mapper['H3O+']]

	#******************************** OH+ **********************************
	S[mapper['OH+']] 	= ((J02) \
				+ (I01)*n[mapper['e']] \
				+ (I08)*n[mapper['eh']] \
				+ (K03)*n[mapper['H+']] \
				+ (K07)*n[mapper['O+']]) * n[mapper['OH']] \
				+ ((J13) \
				+ (ID03)*n[mapper['e']] \
				+ (ID05)*n[mapper['eh']]) * n[mapper['H2O']] \
				+ ((K16)*n[mapper['O']] \
				+ (K18)*n[mapper['OH']]) * n[mapper['H2+']] \
				+ ((K21)*n[mapper['O+']]) * n[mapper['H2']] 				

	L[mapper['OH+']] 	= ((RD01)*n[mapper['e']] \
				+ (RD06)*n[mapper['eh']] \
				+ (K09)*n[mapper['OH']] \
				+ (K10 + K11)*n[mapper['H2O']] \
				+ (K24)*n[mapper['H2']]) * n[mapper['OH+']]

	#******************************** H+ ***********************************
	S[mapper['H+']] 	= ((J06) \
				+ (I02)*n[mapper['e']] \
				+ (I06)*n[mapper['eh']] \
				+ (K01)*n[mapper['H+']] \
				+ (K05)*n[mapper['O+']]) * n[mapper['H']] \
				+ (J09) * n[mapper['H2']] \
				+ ((J11) \
				+ (ID01)*n[mapper['e']] \
				+ (ID04)*n[mapper['eh']]) * n[mapper['H2O']]

	L[mapper['H+']] 	= ((R01)*n[mapper['e']] \
				+ (R04)*n[mapper['eh']] \
				+ (K01)*n[mapper['H']] \
				+ (K02)*n[mapper['O']]
				+ (K03)*n[mapper['OH']] \
				+ (K04)*n[mapper['H2O']] \
				+ (K14)*n[mapper['H2']]) * n[mapper['H+']]

	#******************************** H2+ **********************************
	S[mapper['H2+']] 	= ((J07) \
				+ (K14)*n[mapper['H+']] \
				+ (K15)*n[mapper['H2+']]) * n[mapper['H2']]

	L[mapper['H2+']] 	= ((RD04)*n[mapper['e']] \
				+ (RD05)*n[mapper['eh']] \
				+ (K15)*n[mapper['H2']] \
				+ (K16)*n[mapper['O']] \
				+ (K17 + K18)*n[mapper['OH']] \
				+ (K19 + K20)*n[mapper['H2O']]) * n[mapper['H2+']]

	#******************************** O+ ***********************************
	S[mapper['O+']] 	= ((J01) \
				+ (I03)*n[mapper['e']] \
				+ (I07)*n[mapper['eh']] \
				+ (K02)*n[mapper['H+']] \
				+ (K06)*n[mapper['O+']] \
				+ (K22)*n[mapper['O++']]) * n[mapper['O']] \
				+ ((J12) \
				+ (ID02)*n[mapper['e']] \
				+ (ID06)*n[mapper['eh']]) * n[mapper['H2O']] \
				+ ((R03)*n[mapper['e']] \
				+ (R06)*n[mapper['eh']]) * n[mapper['O++']]

	L[mapper['O+']] 	= ((I05 + R02)*n[mapper['e']] \
				+ (I10 + R05)*n[mapper['eh']] \
				+ (K05)*n[mapper['H']] \
				+ (K06)*n[mapper['O']] \
				+ (K07)*n[mapper['OH']] \
				+ (K08)*n[mapper['H2O']] \
				+ (K21)*n[mapper['H2']]) * n[mapper['O+']]

	#******************************** O++ **********************************
	S[mapper['O++']] 	= ((I05)*n[mapper['e']] \
				+ (I10)*n[mapper['eh']]) * n[mapper['O+']] \
				+ ((K23)*n[mapper['O++']]) * n[mapper['O']]

	L[mapper['O++']] 	= ((R03)*n[mapper['e']] \
				+ (R06)*n[mapper['eh']] \
				+ (K22 + K23)*n[mapper['O']]) * n[mapper['O++']]

	#***********************************************************************
	# Calculate the sources for electrons. Should you just be
	# imposing charge neutrality here instead? NO! Thats bullshit. Only 
	# impose charge neutrality for MHD.
	#***********************************************************************
	S[mapper['e']] 		= ((J11 + J12 + J13 + D02 + 2*(I04 + ID01 + ID02 + ID03)) \
				+ (D05 + 2*(I09 + ID04 + ID05 + ID06))*n[mapper['eh']]) * n[mapper['H2O']] \
				+ ((J02 + D01 + 2*I01) \
				+ (D04 + 2*I08)*n[mapper['eh']]) * n[mapper['OH']] \
				+ ((J06 + 2*I02) \
				+ 2*(I06)*n[mapper['eh']]) * n[mapper['H']] \
				+ ((J07 + J09 + D03) \
				+ (D06)*n[mapper['eh']]) * n[mapper['H2']] \
				+ ((J01 + 2*I03) \
				+ 2*(I07)*n[mapper['eh']]) * n[mapper['O']] \
				+ ((2*I05) \
				+ 2*(I10)*n[mapper['eh']]) * n[mapper['O+']]

	#***********************************************************************
	# Calculate the losses for the electrons.
	#***********************************************************************
	L[mapper['e']] 		= ((D02 + I04 + ID01 + ID02 + ID03) * n[mapper['H2O']] \
				+ (D01 + I01) * n[mapper['OH']] \
				+ (I02) * n[mapper['H']] \
				+ (D03) * n[mapper['H2']] \
				+ (I03) * n[mapper['O']] \
				+ (I05 + R02) * n[mapper['O+']] \
				+ (R01) * n[mapper['H+']] \
				+ (R03) * n[mapper['O++']] \
				+ (RD01) * n[mapper['OH+']] \
				+ (RD02) * n[mapper['H2O+']] \
				+ (RD03) * n[mapper['H3O+']] \
				+ (RD04) * n[mapper['H2+']]) * n[mapper['e']]

	#***********************************************************************
	# Losses for hot electrons.
	#***********************************************************************
	L[mapper['eh']] 	= ((D05 + I09 + ID04 + ID05 + ID06) * n[mapper['H2O']] \
			  	+ (D04 + I08) * n[mapper['OH']] \
			  	+ (I06) * n[mapper['H']] \
			  	+ (D06) * n[mapper['H2']] \
			  	+ (I07) * n[mapper['O']] \
			  	+ (I10 + R05) * n[mapper['O+']] \
			  	+ (R04) * n[mapper['H+']] \
			  	+ (R06) * n[mapper['O++']] \
			  	+ (RD06) * n[mapper['OH+']] \
			  	+ (RD07) * n[mapper['H2O+']] \
			  	+ (RD08) * n[mapper['H3O+']] \
			  	+ (RD05) * n[mapper['H2+']]) * n[mapper['eh']]
	
	r = S - L
	return r
