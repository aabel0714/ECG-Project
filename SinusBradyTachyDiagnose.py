# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 13:36:43 2019

@author: Abel
"""

def SinusBradyDiagnose(HeartRate):
    
    #float heartrate to make sure it is a readable number
    HeartRate = float(HeartRate)
    
    #initialize diagnosis number
    Diagnosis = 0
    
    #testing for either condition dependent upon the bpm
    if (HeartRate) < 60.0:
        print("Diagnosis: Sinus Bradycardia detected")
        #update diagnosis number if applicable
        Diagnosis = 1
    elif (HeartRate) > 100.0:
        print("Diagnosis: Sinus Tachycardia detected")
        #update diagnosis number if applicable
        Diagnosis = 2

    
        
        
    return(Diagnosis)
    