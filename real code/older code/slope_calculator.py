
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import itertools as it
import os

empty = []
for filename in os.listdir("/Users/sameersingh/Downloads/txtfiles"):
    if filename.endswith(".txt"): 
        empty.append(os.path.join("/Users/sameersingh/Downloads/txtfiles", filename))

counter = 0
counter2 = 0
for name in empty:
    df = pd.read_csv(str(name), delimiter=',')
    counter = counter + 1
    df.to_csv('kepler' + str(counter) + 'k.csv')


for filename in os.listdir('/Users/sameersingh/Downloads/keplers'):
    counter2 = counter2 + 1
    plt.figure()
    data = np.genfromtxt(str(filename), delimiter=',', names=["x", "y"])
    data = np.delete(data, 0)
    data_list.append(data)
    plt.plot(data['x'], data['y'])
    plt.show()
    slopes = []
    deltax = []
    
    for x in zip(data, data[1:]):
        delx = (x[counter2][1][0]-x[counter2][0][0])
        slope = (x[counter2][1][1]-x[0][1])/(x[counter2][1][0]-x[0][0])
        slopes.append(slope)
        deltax.append(delx)

    slope_changes_real = []
    slope_changes = [slope2 - slope1 for slope1, slope2 in zip(slopes[: -1], slopes[1 :])] 
    import itertools
    new_list = [x for x in itertools.chain.from_iterable(itertools.zip_longest(slope_changes,deltax)) if x]
    successive_quotients = [m/d for m,d in zip(new_list[: -1], new_list[1: ])]
    sq = []
    for i in range(0, len(successive_quotients), 2):  
        sq.append(successive_quotients[i])

print(len(sq))
#perhaps need to interpolate and phase fold before this method could be viable, but it is ultimately the same that we will always use
