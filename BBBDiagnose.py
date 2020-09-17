# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 15:00:43 2019

"""
import numpy as np

#Need to take index of peaks of R wave - Q wave * time step to get time

def BBBDiagnose(Peaks,timestep,ecgfilt):
    
    #initializing diagnosis number
    Diagnosis = 0
    if len(Peaks[1]) == len(Peaks[2]) and len(Peaks[0]) == len(Peaks[1]):
        timestep = float(timestep)
        
        #looping through the range in which the q wave must begin to find where it
        #first equals zero then adds that to the orignial ecg index list then multiplies
        #by timestep
        
        Qbound1 = (ecgfilt[Peaks[0][0]:Peaks[1][0]])
        Qbound = Qbound1[::-1]
        for i in range(len(Qbound)):
            if Qbound[i] == 0:
                Qindex = 0
                Qindex = i
                break
        Qindex = 0
        #finding index where Q waves sarts
        Qbound = Peaks[1][0]-Qindex                 
        
        #Looping forward through range from S peak to T peak to find where it 
        #first equals 0
        Sbound = ecgfilt[Peaks[3][0]:Peaks[4][0]]
        for i in range(len(Sbound)):
            if Sbound[i] == 0:
                index = 0
                index = i
                break
        index = 0
        
        #finding index of where S wave ends
        Sbound = Peaks[3][0] + index
        
        #calculating the QRS interval time
        QRStime = (Sbound * timestep) - (Qbound * timestep)

        #testing if interval exceeds given duration 
        if QRStime > .07:
            print("Diagnosis: Bundle Branch Block detected")
            #update diagnosis number
            Diagnosis = 3
    else:
        Sbound = 0
        Qbound = 0
    
    return(Sbound,Qbound,Diagnosis)