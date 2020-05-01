#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 14:59:49 2020

@author: tfield
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_table('all_month.csv', delimiter=',')

binList = [];
for i in range(0,11):
    binList.append(i)


plt.figure()
#Removes non finite values and nonnumbers
plt.hist(data['mag'].dropna(), bins=binList)
plt.grid(True)
plt.show()

plt.figure()
ax = data['mag'].plot.kde(bw_method=.25)
ax.grid(True)

plt.figure()
plt.plot(data['longitude'], data['latitude'], '.k')
plt.grid(True)

# Normalized CDF plot of depth
plt.figure()


# Magnitude vs depth scatter plot
plt.figure()
plt.plot(data['mag'], data['depth'], '.k')
plt.grid(True)

#Q-Q plot of magnitudes






