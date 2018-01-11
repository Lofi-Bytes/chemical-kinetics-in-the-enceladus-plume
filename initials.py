# -*- coding: utf-8 -*-

#***********************************************************************
# Importing everything python needs in order to be smart.
#***********************************************************************
import numpy as np                                      			# Numpy tells python how to do array operations.

#***********************************************************************
# Declaring constants for conversions.
#***********************************************************************
A    = 6.022E23                                                     # Avagadro's Number.
uh20 = 18.01528 													# Molar mass of water [g/mol].

#***********************************************************************
# Declaring the initial values.
# At Enceladus, measurements suggest that the neutrals ejected
# from the south polar plume sources have a surface number density
# on the order of 1e10 - 1e11 [cm^{-3}]. Thus each of our
# computational cell represents gas trapped in a cubic centimeter box.
# These densities seem low compared to our experience here on Earth.
# Water vapor at STP has a much higher density than in the near
# vacuum of Saturn's space environment + the extremely cold
# temperatures. At 1x10^{-9} atm (101.3 microPa), 10 degrees Celsius,
# water has a density of 7.754e-10 and is in a gaseous phase.
# Doing the conversion from [g/cm^{3}] to [# molecules/cm^{3}]
# we get a base number density of 2.59e10 [molecules/cm^{3}].
# This value changes, directly proportionally, by an order of
# magnitude for every order of magnitude increase/decrease
# in the pressure. One thing not considered here is that the
# gas must be feeling pressure from itself, ie. a small differential
# element of gas would feel pressure from all of its neighboring
# differential elements of gas. Since the pressure is not exactly
# known, this was the best educated guess I could come up with
# for now. The literature I have read so far, only constrains the
# density to between 1e10 - 1e11 [cm^{-3}]. That is all I have
# to go off of, so to get the number densities in that range I worked
# my way backward to get some kind of constraint on the pressure
# and temperature. Though neither of those things are yet considered
# in this simple model. For comparison, liquid water at STP has a
# number density of ~3e22 [cm^{-3}].
#***********************************************************************
Q0_m  = 2.59e10		 													# Set the surface (initial) number density of (pure) water [(# molecules) * cm^{-3}].
#Q0_m = 2.59e3		 													# Set the surface (initial) number density of (pure) water [(# molecules) * cm^{-3}].
Q0    = Q0_m*uh20/A 													# Convert this number to grams [g] (simply for perspective).

#Q0_eh = 1.0e2															# Set the initial number density for the hot electron population.

#***********************************************************************
# Define the domain of the solution and the size of the timestep.
#***********************************************************************
[tmin, tmax, dt] = [0.0, 1.0e8, 100] # Runs for 120 days.
#[tmin, tmax, dt] = [0.0, 1.0e4, 0.25] # Runs for 0.1 days.

#***********************************************************************
# If we assume that the gas has a constant velocity, then the
# timesteps are directly correlated to the altitude of the gas.
# Measurements suggest v_0 ~ 300 [m/s].
#***********************************************************************
v_0 = 3.0e4 															# Given in units of [cm/s] since our cells are measured in centimeters.

#***********************************************************************
# Define the total number of required iterations.
#***********************************************************************
nmax = int((tmax - tmin)/dt + 1)

#***********************************************************************
# Define time.
#***********************************************************************
t = np.linspace(0, nmax, nmax)*dt + tmin

#***********************************************************************
# Define distance.
#***********************************************************************
distance = v_0*t
