#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 14:59:49 2020

This script reads in a CSV file from the USGS that contains all recorded earthquakes
for the past 30 days. It is downloaded from https://earthquake.usgs.gov/earthquakes/feed/v1.0/csv.php
by selecting the link for 'All Earthquakes' under the 'Past 30 Days' Header on the
right side of the page. Once loaded, six plots are generated based on the data:
    -histogram of magnitudes
    -KDE of magnitudes
    -scatter of latitude/longitude
    -CDF of depths
    -scatter of magnitude vs depth
    -Q-Q of magnitude
Plots are outputted as PNG files for convenience

@authors: tfield
@github: tfield156

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as ss

#Read in data from CSV file
data = pd.read_table('all_month.csv', delimiter=',')

#Create 10 bins for histogram
binList = [];
for i in range(0,11):
    binList.append(i)


# Earthquake magnitude histogram
plt.figure(figsize=(9,6.5))
#Removes non finite values and nonnumbers
plt.hist(data['mag'].dropna(), bins=binList)
plt.grid(True)
plt.title('Earthquake Magnitude Distribution - Field')
plt.xlabel('Magnitude')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('Fig1_MagHistogram.png',dpi=96)

# Earthquake magnitude KDE
plt.figure(figsize=(9,6.5))
ax = data['mag'].plot.kde(bw_method=.25)
ax.grid(True)
plt.title('Earthquake Magnitude Distribution - Field')
plt.xlabel('Magnitude')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('Fig2_MagKDE.png',dpi=96)

# Earthquake Positions lat/long
plt.figure(figsize=(9,6.5))
plt.plot(data['longitude'], data['latitude'], '.k')
plt.title('Earthquake Positions - Field')
plt.xlabel('Longitude (deg)')
plt.ylabel('Latitude (deg)')
plt.grid(True)
plt.tight_layout()
plt.savefig('Fig3_LatLongScatter.png',dpi=96)

# Normalized CDF plot of depth (using histogram with many bins)
plt.figure(figsize=(9,6.5))
plt.hist(data['depth'], cumulative=True,bins=100,density=1)
plt.xlabel('Depth (km)')
plt.ylabel('Cumulative Density')
plt.title('Cumulative Density of Earthquake Depths - Field')
plt.grid(True)
plt.tight_layout()
plt.savefig('Fig4_DepthCDF.png',dpi=96)

# Magnitude vs depth scatter plot
plt.figure(figsize=(9,6.5))
plt.plot(data['mag'], data['depth'], '.k')
plt.grid(True)
plt.tight_layout()
plt.title('Earthquake Depth Distribution - Field')
plt.xlabel('Magnitude')
plt.ylabel('Depth (km)')
plt.savefig('Fig5_MagDepthScatter.png',dpi=96)

#Q-Q plot of magnitudes
plt.figure(figsize=(9,6.5))
ss.probplot(data['mag'],dist='norm',plot=plt)
plt.title('Earthquake Magnitude Q-Q Plot - Field')
plt.grid(True)
plt.tight_layout()
plt.savefig('Fig6_DepthQQ.png',dpi=96)



