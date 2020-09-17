# -*- coding: utf-8 -*-
"""
# course: bmen207-tamu
# date: Summer/19
# description: Python computing0106-File Handling
    
"""
#script to read in sine.txt

import numpy as np
import matplotlib.pyplot as plt
#open file using permission character encoding
fileid=open('sine.txt','r')

##identify data types using the dtype string (i.e. format specifier, such as float)
data=np.loadtxt(fileid,'float32')
[r,c]=np.shape(data)
data=np.squeeze(np.reshape(data,[1,r*c]))  #reshape to 1D array

#close the file
fileid.close()

#reshape into array, no checks
a=len(data)
sine=np.reshape(data,[2,int(a/2)])  #reshape to x column, y column
plt.plot(sine[0,:],sine[1,:])