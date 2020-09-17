# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 16:31:02 2019


"""

import numpy as np
import matplotlib.pyplot as plt
import pylab
from readfile import readecg
from HeartRate import findHeartRate
from PeakFunction import myPeakFinder
from SinusBradyTachyDiagnose import SinusBradyDiagnose
from scipy.signal import find_peaks
from BBBDiagnose import BBBDiagnose
from afibDiagnose import afibDiagnose
from arrDiagnose import arrDiagnose
from av1Diagnosis import av1Diagnose
from av2Diagnose import av2Diagnose
from NoiseRemover import MovNoiseRemover
from scipy import signal


filename = input("Input name of file: ")

#code below reads ecg through the readecg function and finds the peaks of each 
#function. Each diagnose function uses different parameters depending on what
#can be diagnosed with. 

ecg = readecg(filename)

#returns filtered ecg graph 
ecgfilt = MovNoiseRemover(ecg[0],ecg[1])  

#locates all prominent/important peaks for P,Q,R,S,and T waves
Peaks = myPeakFinder(ecg[0],ecgfilt)


#function to find heart rate returns heart rate and timestep
HeartRate = findHeartRate(ecg[0],Peaks[0],ecg[2],ecgfilt)
  

#establisihing the diagnosis number variables for use in determining which
#diagnosis to print later
Diagnose1 = 0
Diagnose2 = [0,0,0]
Diagnose3 = 0
Diagnose4 = 0
Diagnose5 = 0
Diagnose6 = 0

#first determines if the diagnosis is sinus brady or tachy cardia - 
#if it is then it skips the other diagnosis
#if it isn't the elif runs all other diagnostic functions
if HeartRate[0] < 60 or HeartRate[0] > 100:
    
    Diagnose1 = SinusBradyDiagnose(HeartRate[0])
    
elif HeartRate[0] >= 60 and HeartRate[0] <=100:
    
    Diagnose2 = BBBDiagnose(Peaks,HeartRate[1],ecgfilt)
    
    Diagnose3 = afibDiagnose(Peaks)
    
    Diagnose4 = arrDiagnose(Peaks,HeartRate[1])
    
    Diagnose5 = av1Diagnose(Peaks, HeartRate[1])
    
    Diagnose6 = av2Diagnose(Peaks, HeartRate[1])



#The list below contains a number that is updated from zero in the file that
#the diagnose is true in and then using the max function I can find the number
#from that list and use it to set a variable name for the title of the graph.

DiagnoseNumList = [Diagnose1, Diagnose2[2], Diagnose3, Diagnose4, Diagnose5, Diagnose6]
DiagnoseNum = max(DiagnoseNumList)

if DiagnoseNum == 1:
    Diagnosis = 'Sinus Bradycardia'
elif DiagnoseNum == 2:
    Diagnosis = 'Sinus Tachycardia'
elif DiagnoseNum == 3:
    Diagnosis = 'Bundle Branch Block'
elif DiagnoseNum == 4:
    Diagnosis = 'Atrial Fibrillation'
elif DiagnoseNum == 5:
    Diagnosis = 'Sinus Arrhythmia'
elif DiagnoseNum == 6:
    Diagnosis = 'First-degree atrioventricular block'
elif DiagnoseNum == 7:
    Diagnosis = 'Second-degree atrioventricular block'
elif DiagnoseNum == 0:
    Diagnosis = 'Normal Heart Conditions'
    print("Diagnosis: Healthy")

#plot the graph
xaxis = ecg[1]
plt.plot(xaxis,ecgfilt)
pylab.xlabel('Seconds (ms)')
pylab.ylabel('Amplitude (normalised)')
pylab.title(Diagnosis)
pylab.show()