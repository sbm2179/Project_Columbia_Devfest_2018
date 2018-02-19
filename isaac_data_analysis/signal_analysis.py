import numpy as np
from scipy.signal import argrelextrema

#import matplotlib.pyplot as plt
#plt.switch_backend('agg')

def find_local_extrema(y):
    loc_max = argrelextrema(y, np.greater)[0]
    loc_min = argrelextrema(y, np.less)[0]
    return loc_max, loc_min

#Plot min/max points as vertical lines
"""
plt.figure(figsize=(20,10))
plt.plot(range(x), y, 'k')
for i in range(len(loc_max)):
    plt.axvline(x=loc_max[i], color='b', linewidth=1.5)
for i in range(len(loc_min)):
    plt.axvline(x=loc_min[i], color='r', linewidth=2)
plt.savefig('plot.pdf')
plt.show()
"""

#max in blue, min in red
