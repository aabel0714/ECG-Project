# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 14:04:35 2019

"""

def arrDiagnose(Peaks,timestep):
    
    #initializing variables
    Diagnosis = 0
    timestep = float(timestep)
    PintList = []
    RintList = []
    
    #using conditional statements for the amount of peaks to differentiate
    #from other conditions
    if len(Peaks[1]) == len(Peaks[2]):
        if len(Peaks[1]) == len(Peaks[4]):
            
            #using the P and Q index points to find the PP and RR intervals
            Plowbound = Peaks[0][0]
            Phighbound = Peaks[0][1]
            
            Rlowbound = Peaks[2][0]
            Rhighbound = Peaks[2][1]
            
            Pinterval = (Phighbound * timestep) - (Plowbound * timestep)
            Rinterval = (Rhighbound * timestep) - (Rlowbound * timestep)
            
            #getting length of list for P index
            counter = 0
            i = 0
            for i in Peaks[0]:
                counter += 1
            
            #looping and finding all P intervals
            for i in range(0,counter-1):  
                Plowbound = Peaks[0][i]
                Phighbound = Peaks[0][i+1]
                
                Pinterval = (Phighbound * timestep) - (Plowbound * timestep)                
                PintList.append(Pinterval)
             
            #establishing variable for length of R list
            count = 0
            i = 0
            for i in Peaks[2]:
                count += 1
            
            #loopoing and finding all R intervals
            for i in range(0,count-1):  
                Rlowbound = Peaks[2][i]
                Rhighbound = Peaks[2][i+1]
                
                Rinterval = (Rhighbound * timestep) - (Rlowbound * timestep)                
                RintList.append(Rinterval)
                        
            #Finidng smallest intervals in each list
            LowPint = min(PintList)
            LowRint = min(RintList)
            
            #Finding largest intervals in each list
            HighPint = max(PintList)
            HighRint = max(RintList)
            
            #finding the biggest difference between the highest and lowest intervals
            PwaveInt = HighPint - LowPint 
            RwaveInt = HighRint - LowRint
            
            #testing if the difference is bigger than .16
            if PwaveInt > .16 or RwaveInt > .16:
                print("Diagnosis: Sinus Arrhythmia detected")
                Diagnosis = 5
    
    return(Diagnosis)