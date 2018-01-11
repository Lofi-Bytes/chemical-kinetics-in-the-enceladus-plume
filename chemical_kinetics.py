# -*- coding: utf-8 -*-

#***********************************************************************
# Importing everything python needs in order to be smart.
#***********************************************************************
import numpy as np                                      			# Numpy tells python how to do array operations.
import matplotlib.pyplot as plt                         			# Matplotlib tells python how to make pretty plots.
import matplotlib.gridspec as gridspec 								# Make subplots on a custom grid.
import enceladus_programs as ep                       				# Importing my custom library.
import cPickle
import time
import snl
import initials
import mapper
reload(ep)
reload(snl)
reload(initials)
reload(mapper)
from scipy.integrate import odeint
from snl import f
from mapper import *
from initials import *

#***********************************************************************
# Start timing the program.
#***********************************************************************
start = time.time()

#***********************************************************************
# Setting the initial condition. Densities of Each species are given
# in units of [m^-3]. 		 												   
#***********************************************************************
n0 = np.zeros((len(species),))
n0[mapper['H2O']] = Q0_m
#n0[mapper['eh']]  = Q0_eh

#***********************************************************************
# Integrate.
#***********************************************************************
n = odeint(f, n0, t)

# n = ode(f,n0,t, )

#***********************************************************************
# Pickle-Dump all of the arrays to file!
#***********************************************************************
f_out = open('rk4_densities.pkl','w')
cPickle.dump(n, f_out)
f_out.close()

#***********************************************************************
# Print how long it took to run the simulation.
#***********************************************************************
end = time.time()
print "Total time to completion: %f seconds!" % (end - start)
