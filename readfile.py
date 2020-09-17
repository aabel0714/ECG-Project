# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 23:40:40 2019

"""

import numpy as np
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from scipy import signal
from random import randint

def readecg(filename):
    #opening/reading file
    lineslist = []
    with open(filename) as file:
        for line in file: 
            line = line.strip() 
            lineslist.append(line)
   
    #splitting the header line into indexable elements
    HeaderLine = lineslist[0].split(" ")

    #data points and timestep from headerline
    dp = int(HeaderLine[11])
    timestep = float(HeaderLine[8])
    
    print('Patient Number: ',HeaderLine[2])
    print('Lead Number: ', HeaderLine[5])
    
    #removing the header line so the list can be manipulated
    lineslist.remove(lineslist[0])
    
    #converting all numeric strings into floats
    floatlist = []
    for lines in lineslist:
        fline = float(lines)
        floatlist.append(fline)
        
    #defining the x axis using the data points from the header
    xaxis = np.linspace(0,dp,dp)
    
    ecglist = floatlist
    
    ecg = signal.detrend(ecglist)
    
    #adding noise
#    randnum = randint(0,15) * .01
#    print("Noise %",randnum)
    
#    noise_amplitude = max(ecg)*randnum

    noise = 0

    ecgN = ecg + noise
    
    return(ecgN,xaxis,timestep)

