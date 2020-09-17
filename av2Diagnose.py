# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 22:32:39 2019


"""
import numpy as np
def av2Diagnose(Peaks,timestep):
    
    #initializing diagnosis number
    Diagnosis = 0
    
    #using length of list conditions to diagnose av2
    if (len(Peaks[4]) > len(Peaks[3])):
        Ppeaks = Peaks[0]
        Ppks = np.delete(Ppeaks,0,0)
        
        #using conditional statements to limit the diagnostic possiblities to
        #only av2 conditions
        if (len(Ppks) == len(Peaks[4])) and (len(Peaks[4]) > len(Peaks[3])):
            print("Diagnosis: Second-degree atrioventricular block detected")
            
            #update diagnosis number
            Diagnosis = 7
    return(Diagnosis)