# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 22:56:22 2019

@author: Abel
"""
import numpy as np
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import pylab
from Python_POP6 import HeaderFunction
from scipy import signal

def Detrend(ecg):
    
detrend = signal.detrend(Header)

from matplotlib import pyplot as plt


plt.plot(detrend, label="x")
plt.plot(detrend, label="x_detrended")
plt.show()


#import numpy as np
#t = np.linspace(0, 5, 100)
#x = t + np.random.normal(size=100)
#Detrend


#x_detrended = signal.detrend(x)