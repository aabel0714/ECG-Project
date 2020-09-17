# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 14:12:35 2019


"""
import pylab
import scipy.signal as signal
import numpy as np
import csv 
from scipy.signal import find_peaks
import matplotlib.pyplot as plt
from scipy.signal import peak_prominences

#function to find the peaks and location for desired wave
def myPeakFinder(ecg,ecgfilt): 

    #finding P peaks that are prominent in amplitude by .15 and appending them
    #to a list
    Pwave_list = []
    Pwave_pks = find_peaks(ecgfilt, height = (0.14,0.30), prominence = 0.15)
    for i in Pwave_pks:
        Pwave_list.append(i)
    Ppks = Pwave_list[0]
    
    #finding R peaks that are prominent in amplitude by .1 and appending them
    #to a list
    Rwave_list = []
    Rwave_pks = find_peaks(ecgfilt, height = (0.75), prominence = 0.1)
    for i in Rwave_pks:
        Rwave_list.append(i)
    Rpks = Rwave_list[0]
    
    #finding T peaks that are prominent in amplitude by .15 and appending them
    #to a list
    Twave_list = []
    Twave_pks = find_peaks(ecgfilt, height = (0.35,0.6),prominence = 0.15)
    for i in Twave_pks:
        Twave_list.append(i)
    Tpks = Twave_list[0]
    
    #finding Q and S peaks at the same time by inverting the ecg trace
    Qpks = []
    Spks = []
    SQwavelist = []
    SQwavepks = find_peaks(-ecgfilt, height = (0.20,0.45), prominence = 0.1)
    for i in SQwavepks:
        SQwavelist.append(i)
    SQpks = (SQwavelist[0])
    
    #the peaks will be in a list in a sequence of Q,P,Q,P... ect. so dividing 
    #the index number by 2 and using modulo I can add the first of each pair
    #to a list and the second of each pair to a list
    for i in range(len(SQpks)):
        if i % 2 == 0:
            Qpks.append(SQpks[i])
        if i % 2 != 0:
            Spks.append(SQpks[i])
                 
    
    return(Ppks,Qpks,Rpks,Spks,Tpks)
   