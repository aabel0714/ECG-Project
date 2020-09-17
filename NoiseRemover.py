# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 20:58:00 2019

@author: Abel
"""
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


def MovNoiseRemover(ecg,xaxis):
    
    #using window size of 10 for moving average filter
    window_size = 10
    window = np.squeeze(np.ones([1,window_size])/window_size)
    ecgfilt1 = signal.convolve(ecg,window,mode='same')
    
    #detrending graph if needed
    ecgfilt = signal.detrend(ecgfilt1)
    
    return(ecgfilt)
    