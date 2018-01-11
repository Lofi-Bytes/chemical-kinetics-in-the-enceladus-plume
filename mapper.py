# -*- coding: utf-8 -*-

#***********************************************************************
# Creating lists of all of the neutral and ion species that may be 		   
# present in the plume. 									           
#***********************************************************************
neutrals 	= ['H2O', 'OH', 'H', 'H2', 'O']
ions 		= [ 'H2O+', 'H3O+','OH+', 'H+', 'H2+', 'O+', 'O++']
electrons 	= ['e', 'eh']

species = neutrals + ions + electrons

#***********************************************************************
# Creating an empty dictionary to store array indices.
# Populate with indices.
#***********************************************************************
mapper = {}
for i,s in enumerate(species):
    mapper[s] = i

