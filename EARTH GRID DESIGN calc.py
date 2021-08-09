# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 14:43:21 2020

@author: hmnazif
"""
#IMPORT LIBRARIES

import pandas as pd

import math 

import numpy as np

#DEFINE INPUTS

#AREA OF THE SUBSTATION
    
length_of_substation = input("Enter the length of the substation area in m: ")

breadth_of_substation = input("Enter the breadth of substation area in m: ")

area_of_substation = float(length_of_substation) * float(breadth_of_substation)


#RESISTIVITY OF THE SOIL

res_of_soil = input("Enter resistivity of the soil in μΩ.cm: ")

#ENTER VALUE, DURATION OF RMS CURRENT & AMBIENT TEMPERATURE

current = input("Enter Irms current in kA: ")

current_duration = input("Enter duration of current in s: ")

amb_temp = input("Enter ambient temperature in °C: ")

print("\n")

#IMPORT CONDUCTOR LIBRARY 

conductor_prop = pd.read_csv('C:/Users/hmnazif/Documents/CONDUCTOR PROPERTIES FOR PYTHON EARTH GRID.csv')

print(conductor_prop)


#SELECTING CONDUCTOR TYPE AND REFERENCING VARIABLES FROM PROPERTIES TABLE

print("\n")

print("To select the conductor type, use one of the following codes:\n 0 for Copper annealed soft-drawn\n 1 for copper commercial hard-drawn\n 2 for copper-clad steel wire\n 3 for copper-clad steel rod\n 4 for Copper-Clad steel rod \n 5 for Aluminium EC grade\n 6 for Aluminium 5005 alloy\n 7 for Aluminium 6201 alloy\n 8 for Aluminium-clad steel wire\n 9 for steel 1020\n 10 for Stainless-clad steel rod\n 11 for zinc-coated steel rod\n" )

con_type = input("Enter code for conductor type: ")

con_type = int(con_type)

conductor_type = conductor_prop["Conductor Type"].iloc[con_type]

mat_con = conductor_prop["Material Conductivity"].iloc[con_type]

ar_fact = conductor_prop["ar factor"].iloc[con_type]

ko = conductor_prop["Ko"].iloc[con_type]

fuse_temp = conductor_prop["Fusing Temp"].iloc[con_type]

res_grnd = conductor_prop["ar"].iloc[con_type]

tcap = conductor_prop["TCAP"].iloc[con_type]

#CALCULATING CROSS SECTIONAL AREA OF CONDUCTOR

x = ((float(tcap) * (1/10000))/(float(current_duration) * ar_fact * res_grnd))

y = ((float(ko) + float(fuse_temp))/(float(ko) + float(amb_temp)))

z = (x) * (np.log(y))

cond_cross = (float(current))/(math.sqrt(float(z)))

#PRINT RESULTS/OUTPUT OF THE CALCULATION

print("\n")

print("RESULTS OF THE CALCULATION\n")

print("Length of substation area: " + str(length_of_substation) + "m\n")

print("Breadth of substation area: " + str(breadth_of_substation) + "m\n")

print("Area of substation: " + str(area_of_substation) + "m\n")

print("Resistivity of soil: " + str(res_of_soil) + " μΩ.cm\n")
 
print("Conductor Description: " + str(conductor_type) + "\n")

print("Material conductivity: " +str(mat_con) + "(%)\n")

print("Thermal coefficient of resistivity at reference temperature: " + str(ar_fact) + "°C\n")

print("Ko: " + str(ko) + "\n")

print("Fusing Temperature: " +str(fuse_temp) + "°C\n")

print("Resistivity of the ground conductor at reference temperature Tr: " + str(res_grnd) + "°C\n")

print("Thermal capacity per unit volume: " + str(tcap) + "\n")

print("Conductor Cross-section: " + str(round(cond_cross,2)) + " sq.mm")
