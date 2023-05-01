# -*- coding: utf-8 -*-
"""
Created on Mon May  1 17:38:25 2023

@author: Vite UH
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the data
data = pd.read_csv('data5.csv')
data.columns = ['Weight']

# Create the distribution array
weights, bins = np.histogram(data['Weight'], bins=20, range=(2.5, 4.5))
bins = bins[:-1] + (bins[1] - bins[0])/2

# Calculate the average weight
W = np.average(data['Weight'])

# Calculate the fraction of babies weighing between 0.8W and 1.2W
fraction = np.sum((data['Weight'] >= 0.8*W) &
                  (data['Weight'] <= 1.2*W)) / len(data)

# Plot the histogram
plt.hist(data['Weight'], bins=20, range=(2.5, 4.5), alpha=0.5)
plt.plot(bins, weights, 'ro', label='Distribution')
plt.axvline(W, color='b', linestyle='dashed', linewidth=1,
            label=f'W = {W:.2f} kg')
plt.title('Distribution of Newborn Weights')
plt.xlabel('Weight (kg)')
plt.ylabel('Frequency')
plt.legend()

# Print the fraction of babies weighing between 0.8W and 1.2W
plt.text(2.5, 15,
         f'Fraction of babies between 0.8W and 1.2W = {fraction:.2f} kg')

plt.savefig('Dist of NW.png')
plt.show()
