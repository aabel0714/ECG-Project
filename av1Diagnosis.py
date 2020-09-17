# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 22:13:45 2019

@
"""

def av1Diagnose(Peaks,timestep):
    
    #initializing timestep and diagnosis number
    timestep = float(timestep)
    Diagnosis = 0
    
    #using a conditional statement to exclude other heart conditions
    if len(Peaks[1]) == len(Peaks[2]):
        
        #setting boundries for PR interval
        Pbound = Peaks[0][0]
        Rbound = Peaks[2][0]
        
        #getting times 
        Ptime = Pbound * timestep
        Rtime = Rbound * timestep
        
        #subtract times to get the interval duration
        Interval = Rtime - Ptime
        
        #if diagnosis is true update the diagnostic number
        if Interval > .2:
            print("Diagnosis: First-degree atrioventricular block detected")
            Diagnosis = 6
        
    return(Diagnosis)