#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 21:46:29 2018

@author: dcohen
"""

import matplotlib.pyplot as plt
import pandas as pd

# Read the data file
df = pd.read_csv ("./Logging.txt",  \
                  usecols=(0,1,2,3,4), header=None)

# Assign column names
df.columns=['str_time', 'enc_pos', 'distance', 'velocity', 'accel']

# Rebuild str_time series so that the milliseconds has 3
# decimal points, using slicing
df['millis'] = df.str_time.str[9:]
df['millis'] = df.millis.str.zfill(4) 

# Combine the time string H:H:S with .sss
df['str_time'] = df.str_time.str[ :9] + df['millis']
# I don't need the millis anymore, so delete it
del df['millis']

# Finally, convert str_time to datetime
df['str_time'] = pd.to_datetime(df['str_time'])

# Print some information of the dataframe
#print df
#print df.dtypes

# Let's try plotting some stuff
#fig, axs = plt.subplots(1,2)
#df['enc_pos'].plot(ax=axs[0])
#df['distance'].plot(ax=axs[1])
df.plot('str_time', 'enc_pos')
df.plot('str_time', 'distance')
df.plot('str_time', 'velocity')
df.plot('str_time', 'accel')
plt.show()

print df.describe()

