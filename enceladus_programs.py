# -*- coding: utf-8 -*-

#***********************************************************************
# Importing everything python needs in order to be smart.
#***********************************************************************
import numpy as np                                      					# Numpy tells python how to do array operations.
import matplotlib.pyplot as plt                         					# Matplotlib tells python how to make pretty plots.
import matplotlib.gridspec as gridspec 										# Make subplots on a custom grid.

#***********************************************************************
# Creating lists of all of the neutral and ion species that may be 		   
# present in the plume. 									           
#***********************************************************************
neutrals 	= ['H', 'H2', 'O', 'OH', 'H2O']
ions 		= ['H+', 'H2+', 'O+', 'O++', 'OH+', 'H2O+', 'H3O+']
electrons 	= ['e']

#***********************************************************************
# Defining the conical expansion term. Change the plume angle as
# desiered. Physically speaking, it only makes sense for the angle 
# to range from 0 - pi/2. If zero, simply comment out the expansion
# term in the RK4 solver instead.
#***********************************************************************
def vol(n, dt):
	vol = n / ((1.0/3.0)*np.pi*((1000*dt)**3)*np.tan(np.pi/4)**2)
	return vol



