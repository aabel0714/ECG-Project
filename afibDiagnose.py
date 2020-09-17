# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 13:01:45 2019

"""

def afibDiagnose(Peaks):
    #initializing Diagnosis number in this function
    Diagnosis = 0
    #comparing length of peak lists to determine afib
    if (len(Peaks[1]) > len(Peaks[2]) or len(Peaks[1]) > len(Peaks[3])) or (len(Peaks[4]) == 0):
        print("Diagnosis: Atrial Fibrillation Detected")
        #updating diagnosis number
        Diagnosis = 4
    return(Diagnosis)