# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 14:56:40 2019

"""

import pylab
import scipy.signal as signal
import numpy as np
import csv 
from scipy.signal import find_peaks
import matplotlib.pyplot as plt
from scipy.io import loadmat
from scipy.signal import peak_prominences

def findHeartRate(ecg,pks,timestep,ecgfilt):            #HR = sec/min / sec/beat
    Difflist = []
    #calculating heartbeat in this section using T peaks
    pks = find_peaks(ecgfilt, height = (0.3,0.6), prominence = 0.15)
    
    #using indexes list to find the difference between each peak
    vals = pks[0]
    for i in range(len(vals)-1):
        diff = vals[i+1]-vals[i]
        Difflist.append(diff)

    #calculating using average difference and timestep
    average_diff = np.mean(Difflist)                   
    secbeat = timestep * average_diff  
    HeartRate = (60 / secbeat)
    if HeartRate > 0:
        HR = round(HeartRate,2)
        print("Heart Rate is: ",HR, " bpm")
    
    #this will caluclate heartbeat using R peaks instead of T peaks since afib
    #wont have T peaks.
    if len(pks[0]) == 0:                    
        pks1 = find_peaks(ecgfilt,height = 0.75, prominence = 0.1)
        vals = pks1[0]
        for i in range(len(vals)-1):
            diff = vals[i+1]-vals[i]
            Difflist.append(diff)
        
        #finding the average difference between the peaks and using it to calculate
        #the heartbeat
        average_diff = np.mean(Difflist)   
        secbeat = timestep * average_diff  
        HeartRate = (60 / secbeat)
        
        #rounding heartrate to two decimal places
        HR = round(HeartRate,2)
        print("Heart Rate is: ",HR, " bpm")
    return(HR,timestep)                          

