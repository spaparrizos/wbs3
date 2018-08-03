#!/usr/bin/env python
############################################### SECTION 0 #############################################

# Python libraries
import numpy as np, netCDF4, os, sys
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

############################################### SECTION 1 #############################################

meteo_res = 24
Ybegin = 2008
Yend = 2010
days = [31, 29 if year%4==0 else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
cumdays = np.cumsum(days)
cumvalues = np.append(0, cumdays*meteo_res) 
years = range(Ybegin,Yend+1)
nyears=len(years)
nmonths = 12
ndays = 365
path_input = "/home/surface2/spaparri/WBS3/WBS3/wbs3/Sani_Chalkidiki/Sani_2008.txt"



# Read txt file(s)
data = pd.read_csv(path_input, sep="	", header=None)
print data

list_data = list(data)
print data[0]


for idata in enumerate(list_data):
    print idata
    data[idata] = data[0][:]


print data[0].shape

print data[0].mean(), data[1].mean()









raw_input("C")


