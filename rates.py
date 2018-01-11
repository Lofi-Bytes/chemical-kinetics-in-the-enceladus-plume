# -*- coding: utf-8 -*-

#***********************************************************************
# Charge exchange reactions / rates given in [cm^3/s].                          
#***********************************************************************

# Most Important Reactions
K01 = 9.7E-9  #* 1E-6 	# H+   + H   → H   + H+		*
K02 = 3.0E-9  #* 1E-6 	# H+   + O   → H   + O+
K03 = 3.0E-10 #* 1E-6 	# H+   + OH  → H   + OH+
K04 = 2.0E-8  #* 1E-6 	# H+   + H2O → H   + H2O+
K05 = 3.4E-9  #* 1E-6 	# O+   + H   → O   + H+
K06 = 6.2E-9  #* 1E-6 	# O+   + O   → O   + O+		*
K07 = 3.0E-10 #* 1E-6 	# O+   + OH  → O   + OH+
K08 = 2.3E-9  #* 1E-6 	# O+   + H2O → O   + H2O+
K09 = 7.0E-10 #* 1E-6 	# OH+  + OH  → O   + H2O+
K10 = 1.3E-9  #* 1E-6 	# OH+  + H2O → O   + H3O+
K11 = 1.6E-9  #* 1E-6 	# OH+  + H2O → OH  + H2O+
K12 = 2.1E-9  #* 1E-6 	# H2O+ + H2O → OH  + H3O+
K13 = 7.9E-9  #* 1E-6 	# H2O+ + H2O → H2O + H2O+	*

# Less Important Reactions
K14 = 1.6E-9  #* 1E-6 	# H+   + H2  → H  + H2+
K15 = 3.6E-9  #* 1E-6 	# H2+  + H2  → H2 + H2+		*
K16 = 1.0E-9  #* 1E-6 	# H2+  + O   → H  + OH+
K17 = 7.6E-10 #* 1E-6 	# H2+  + OH  → H  + H2O+
K18 = 7.6E-10 #* 1E-6 	# H2+  + OH  → H2 + OH+
K19 = 3.4E-9  #* 1E-6 	# H2+  + H2O → H  + H3O+
K20 = 3.9E-9  #* 1E-6 	# H2+  + H2O → H2 + H2O+
K21 = 1.6E-9  #* 1E-6 	# O+   + H2  → H  + OH+
K22 = 5.2E-10 #* 1E-6 	# O++  + O   → O+ + O+
K23 = 5.4E-9  #* 1E-6 	# O++  + O   → O  + O++		*
K24 = 1.1E-9  #* 1E-6 	# OH+  + H2  → H  + H2O+
K25 = 6.1E-10 #* 1E-6 	# H2O+ + H2  → H  + H3O+

#***********************************************************************
# Photolytic reaction rates given in [cm^3/s].                          
#***********************************************************************

# Most Important Reactions
J01 = 2.3E-9 #* 1E-6 	# O   + γ → O+  + e
J02 = 3.7E-9 #* 1E-6 	# OH  + γ → OH+ + e
J03 = 5.5E-8 #* 1E-6 	# OH  + γ → O   + H
J04 = 1.1E-7 #* 1E-6 	# H2O + γ → H   + OH
J05 = 1.5E-8 #* 1E-6 	# H2O + γ → H2  + O

# Less Important Reactions
J06 = 8.0E-10 #* 1E-6 	# H   + γ → H+   + e
J07 = 5.9E-10 #* 1E-6 	# H2  + γ → H2+  + e
J08 = 4.9E-10 #* 1E-6 	# H2  + γ → H    + H
J09 = 1.0E-10 #* 1E-6 	# H2  + γ → H+   + H  + e
J10 = 3.7E-9  #* 1E-6 	# H2O + γ → H2O+ + e
J11 = 1.4E-10 #* 1E-6 	# H2O + γ → H+   + OH + e
J12 = 6.4E-11 #* 1E-6 	# H2O + γ → O+   + H2 + e
J13 = 6.1E-10 #* 1E-6 	# H2O + γ → OH+  + H  + e

#***********************************************************************
# Impact dissociation reactions / rates given in [cm^3/s].                          
#***********************************************************************

# Most Important Reactions
D01 = 6.7E-11 #* 1E-6 	# OH  + e  → O  + H + e
D02 = 1.2E-9  #* 1E-6 	# H2O + e  → OH + H + e

# Less Important Reactions
D03 = 1.9E-9  #* 1E-6 	# H2 + e  → H + H + e

#*********************** Hot electron population ***********************

# Most Important Reactions
D04 = 8.4E-8 #* 1E-6 	# OH  + eh → O  + H + e
D05 = 1.5E-6 #* 1E-6 	# H2O + eh → OH + H + e

# Less Important Reactions
D06 = 2.3E-6 #* 1E-6 	# H2 + eh → H + H + e

#***********************************************************************
# Electron impact ionization reactions / rates given in [cm^3/s].                          
#***********************************************************************

# Most Important Reactions
I01 = 5.3E-11 #* 1E-6 	# OH  + e  → OH+  + 2e

# Less Important Reactions
I02 = 1.1E-11 #* 1E-6 	# H   + e  → H+   + 2e
I03 = 1.3E-11 #* 1E-6 	# O   + e  → O+   + 2e
I04 = 7.0E-12 #* 1E-6 	# H2O + e  → H2O+ + 2e
I05 = 2.4E-16 #* 1E-6 	# O+  + e  → O++  + 2e

#*********************** Hot electron population ***********************

# Most Important Reactions
I06 = 3.2E-8 #* 1E-6 	# H   + eh → H+   + 2e
I07 = 9.0E-8 #* 1E-6 	# O   + eh → O+   + 2e
I08 = 1.2E-7 #* 1E-6 	# OH  + eh → OH+  + 2e
I09 = 9.1E-8 #* 1E-6 	# H2O + eh → H2O+ + 2e

# Less Important Reactions
I10 = 2.7E-8 #* 1E-6 	# O+  + eh → O++  + 2e

#***********************************************************************
# Electron impact ionization-dissociation reactions / rates 
# given in [cm^3/s].                          
#***********************************************************************

# Most Important Reactions

# Less Important Reactions
ID01 = 5.3E-14 #* 1E-6 	# H2O + e  → H+  + OH + 2e
ID02 = 3.2E-15 #* 1E-6 	# H2O + e  → O+  + 2H + 2e
ID03 = 1.1E-12 #* 1E-6 	# H2O + e  → OH+ + H  + 2e

#*********************** Hot electron population ***********************

# Most Important Reactions
ID04 = 4.1E-8 #* 1E-6 	# H2O + eh → H+  + OH + 2e
ID05 = 4.5E-8 #* 1E-6 	# H2O + eh → OH+ + H  + 2e

# Less Important Reactions
ID06 = 1.1E-8 #* 1E-6 	# H2O + eh → O+  + 2H + 2e

#***********************************************************************
# Electron recombination reactions / rates given in [cm^3/s].                          
#***********************************************************************

# Most Important Reactions

# Less Important Reactions
R01 = 8.5E-11 #* 1E-6 	# H+  + e  → H
R02 = 3.2E-13 #* 1E-6 	# O+  + e  → O
R03 = 1.9E-12 #* 1E-6 	# O++ + e  → O+

#*********************** Hot electron population ***********************

# Most Important Reactions

# Less Important Reactions
R04 = 6.4E-12 #* 1E-6 	# H+  + eh → H
R05 = 3.0E-13 #* 1E-6 	# O+  + eh → O
R06 = 1.5E-12 #* 1E-6 	# O++ + eh → O+

#***********************************************************************
# Dissociative electronic recombination reactions / rates
# given in [cm^3/s].                          
#***********************************************************************

# Most Important Reactions
RD01 = 9.6E-9 #* 1E-6 	# OH+  + e → O  + H
RD02 = 2.0E-8 #* 1E-6 	# H2O+ + e → OH + H
RD03 = 1.4E-8 #* 1E-6 	# H3O+ + e → OH + H2

# Less Important Reactions
RD04 = 2.0E-8 #* 1E-6 	# H2+  + e  → H  + H

#*********************** Hot electron population ***********************
# Most Important Reactions
D04  = 8.4E-8  #* 1E-6 	# OH   + eh → O  + H + e
D05  = 1.5E-6  #* 1E-6 	# H2O  + eh → OH + H + e
D06  = 2.3E-6  #* 1E-6 	# H2   + eh → H  + H + e
R04  = 6.4E-12 #* 1E-6 	# H+   + eh → H
R05  = 3.0E-13 #* 1E-6 	# O+   + eh → O
R06  = 1.5E-12 #* 1E-6 	# O++  + eh → O+
RD05 = 2.0E-8  #* 1E-6 	# H2+  + eh → H  + H	
RD06 = 1.1E-9  #* 1E-6 	# OH+  + eh → O  + H
RD07 = 8.9E-11 #* 1E-6 	# H2O+ + eh → OH + H
RD08 = 4.7E-11 #* 1E-6 	# H3O+ + eh → OH + H2
I06  = 3.2E-8  #* 1E-6 	# H    + eh → H+   + 2e
I07  = 9.0E-8  #* 1E-6 	# O    + eh → O+   + 2e
I08  = 1.2E-7  #* 1E-6 	# OH   + eh → OH+  + 2e
I09  = 9.1E-8  #* 1E-6 	# H2O  + eh → H2O+ + 2e
I10  = 2.7E-8  #* 1E-6 	# O+   + eh → O++  + 2e
ID04 = 4.1E-8  #* 1E-6 	# H2O  + eh → H+   + OH + 2e
ID05 = 4.5E-8  #* 1E-6 	# H2O  + eh → OH+  + H  + 2e
ID06 = 1.1E-8  #* 1E-6 	# H2O  + eh → O+   + 2H + 2e

# Less Important Reactions
RD05 = 2.0E-8  #* 1E-6 	# H2+  + eh → H  + H
RD06 = 1.1E-9  #* 1E-6 	# OH+  + eh → O  + H
RD07 = 8.9E-11 #* 1E-6 	# H2O+ + eh → OH + H
RD08 = 4.7E-11 #* 1E-6 	# H3O+ + eh → OH + H2
