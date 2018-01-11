# -*- coding: utf-8 -*-

#***********************************************************************
# Importing everything python needs in order to be smart.
#***********************************************************************
import numpy as np                                      			# Numpy tells python how to do array operations.
import matplotlib.pyplot as plt                         			# Matplotlib tells python how to make pretty plots.
import matplotlib.gridspec as gridspec 								# Make subplots on a custom grid.
import enceladus_programs as ep                       				# Importing my custom library.
import cPickle
import initials
import mapper
import time
reload(initials)
reload(mapper)
reload(ep)
from mapper import *
from initials import *

#***********************************************************************
# Plotting function.
#***********************************************************************
def plot(time, distance, n1, n2, n3, n4, n5, i1, i2, i3, i4, i5, i6, i7, e, eh):
	# Plot Number Density vs Altitude.
	num_plots = 13
	colormap  = plt.cm.gist_ncar
	#colormap  = plt.cm.gist_rainbow
	#colormap  = plt.cm.spectral
	#colormap  = plt.cm.Accent
	#colormap  = plt.cm.hsv
	#colormap  = plt.cm.Set1
	#colormap  = plt.cm.Set2
	#colormap  = plt.cm.Set3
	labels    = ['H$_{2}$O', 'H', 'H$_{2}$', 'O', 'OH', 'H$_{2}$O$^{\\plus}$', 'H$_{3}$O$^{\\plus}$', 'H$^{\\plus}$', 'H$_{2}$$^{\\plus}$', 'O$^{\\plus}$', 'O$^{\\plus\\plus}$', 'OH$^{\\plus}$', 'e', 'e$_{h}$']
	gs        = gridspec.GridSpec(1, 1, width_ratios=[12,1], height_ratios=[26,1])
	fig1      = plt.figure(figsize=[12.15, 7.06])	
	ax1       = plt.subplot(gs[0])	
	plt.gca().set_color_cycle([colormap(i) for i in np.linspace(0.10, 0.90, num_plots)])
	ax1.set_title('Time (Altitude) vs. Number Density')
	ax1.set_ylabel('Number Density $[cm^{-3}]$')
	ax1.set_xlabel('Time $[days]$')
	ax1.set_xlim([0, time[-1]])
	#ax1.set_xlim([0, 1])
	#ax1.set_ylim([1E-16, 5E11])
	#ax1.set_ylim([1E-19, 1E5])
	#ax1.set_ylim([1E13, 1E30])
	ax1.semilogy(time, n1, linewidth=1.5)
	ax1.semilogy(time, n2, linewidth=1.5)
	ax1.semilogy(time, n3, linewidth=1.5)
	ax1.semilogy(time, n4, linewidth=1.5)
	ax1.semilogy(time, n5, linewidth=1.5)
	ax1.semilogy(time, i1, '--', linewidth=2.0)
	ax1.semilogy(time, i2, '--', linewidth=3.0)
	ax1.semilogy(time, i3, '--', linewidth=2.0)
	ax1.semilogy(time, i4, '--', linewidth=1.5)
	ax1.semilogy(time, i5, '--', linewidth=1.5)
	ax1.semilogy(time, i6, '--', linewidth=1.5)
	ax1.semilogy(time, i7, '--', linewidth=1.5)
	ax1.semilogy(time, e, ':', linewidth=4.0)
	ax1.semilogy(time, eh, ':', linewidth=4.0)
	ax1.legend(labels, bbox_to_anchor=(1.025, 1), loc=2, borderaxespad=0., fancybox=False, shadow=False)
	
	# Create the new x-axis for plotting distance next to time.
	ax2 = ax1.twiny()
	
	# Make some room at the bottom for the new axis.
	fig1.subplots_adjust(bottom=0.22)
	
	new_tick_locations = np.linspace(0, np.max(distance), 6)
	
	# Place the new axis at the bottom.
	ax2.set_frame_on(True)
	ax2.patch.set_visible(False)
	ax2.xaxis.set_ticks_position('bottom')
	ax2.xaxis.set_label_position('bottom')
	ax2.spines['bottom'].set_position(('outward', 50))
	#ax2.set_xlabel("Altitude $[km]$ \n Assuming a constant outflow velocity of $300 \\frac{m}{s}$ and a conical expansion angle of $\\theta = \\frac{\\pi}{4}$")
	ax2.set_xlabel("Altitude $[km]$ \n Assuming a constant outflow velocity of $300 \\frac{m}{s}$ \n Parcel in a box, no expansion.")
	ax2.set_xticks(new_tick_locations)
	
	# Save the plot and close it so that it doesn't take up all your memory.
	fig1.savefig('./figures/fig.pdf')
	plt.close()

#***********************************************************************
# Start timing the program.
#***********************************************************************
start = time.time()

#***********************************************************************
# Pickle-Read all of the arrays from file!
#***********************************************************************
f_in = open('rk4_densities.pkl','r')
n = cPickle.load(f_in)
f_in.close()

#***********************************************************************
# Split 2D array into many 1D arrays.
#***********************************************************************
n=n.transpose()

#***********************************************************************
# Plot the results.
#***********************************************************************
plot(t / (60*60*24), distance / (100*1000), n[mapper['H2O']], n[mapper['OH']], n[mapper['H']], n[mapper['H2']], n[mapper['O']], n[mapper['H2O+']], n[mapper['H3O+']], n[mapper['OH+']], n[mapper['H+']], n[mapper['H2+']], n[mapper['O+']], n[mapper['O++']], n[mapper['e']], n[mapper['eh']])

#***********************************************************************
# Print how long it took to run the simulation.
#***********************************************************************
end = time.time()
print "Total time to completion: %f seconds!" % (end - start)

















