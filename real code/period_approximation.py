import numpy as np
from random import uniform
import matplotlib.pyplot as plt
from keplersplinev2 import *
import itertools 
with open("hlsp_k2sff_k2_lightcurve_201613023-c01_kepler_v1_llc-default-aper.txt", "r") as f:
      data = np.genfromtxt(f, delimiter=',', usecols = [0,1], names=["time", "flux"], encoding = "Latin_1")
data = np.delete(data, 0)
input_mask = np.ones_like(data["time"], dtype=np.bool)
input_mask[595:625] = False
s, metadata = choosekeplersplinev2(data["time"], data["flux"], return_metadata=True)
l = list(data["flux"]/s)
xs = list(data["time"])
xy = [x for x in itertools.chain.from_iterable(itertools.zip_longest(xs ,l)) if x]
coords = [xy[x:x + 2] for x in range(0, len(xy), 2)] 
quartiles = np.percentile(l, [25, 50, 75])
iqr = float(quartiles[2] - quartiles[0])
outlier_threshold = float(1.5*iqr) + float(quartiles[1])
revised = [x for x in l if x < outlier_threshold]
revised_x = []
for x, y in coords:
    if y in revised:
        revised_x.append(x)
xy2 = [x for x in itertools.chain.from_iterable(itertools.zip_longest(revised_x ,revised)) if x]
coords2 = [xy2[x:x + 2] for x in range(0, len(xy2), 2)] 
#print(len(coords2) - len(data))
#for i in range(500): 
   # l.append(round(uniform(1,10), 2))
list_of_lists = []
for index in range(len(revised)):
    if index > 19:
        lower = index - 20
        upper = index + 21
        new_list = revised[lower:upper]
        list_of_lists.append(new_list)
    else:
        new_list = revised[0:int(index+21)]
        list_of_lists.append(new_list)
booleans = []
for a,b in zip(revised, list_of_lists):
    if a == min(b):
        booleans.append(True)
    else:
        booleans.append(False)
median_offsets = []
for a,b in zip(booleans, list_of_lists):
    if a is True:
        offset = abs(np.median(b) - min(b))
        median_offsets.append(offset)
    else:
        median_offsets.append(0)
good_list = [x for x in median_offsets if x != 0]
threshold = np.mean(good_list) + 2*np.std(good_list)
final_list = []
for x in median_offsets:
    if x >= threshold:
        final_list.append(x)
    else:
        final_list.append(0)
tuples = []
for a,b in zip(final_list, revised):
    if a != 0:
        g = b
        for x, y in coords2:
            if y == g:
                tuples.append((x,y))
                


#print(tuples)
comparison = []
for x, y in itertools.permutations(tuples, 2):
    comparison.append(((x,y)))
size = len(tuples) - 1
br = [comparison[i * size:(i + 1) * size] for i in range((len(comparison) + size - 1) // size )]  
test = []
for thing in br:
    for thing2 in thing:
        distance = thing2[1][0] - thing2[0][0]
        test.append(abs(distance))
size = len(tuples) - 1
br2 = [test[i * size:(i + 1) * size] for i in range((len(test) + size - 1) // size )]  
#print(br2)

x_coords = []
for x, y in tuples:
    x_coords.append(x)
differences = [x2 - x for x, x2 in zip(x_coords[: -1], x_coords[1 :])] 
average = [x for x in differences if x < 9]
print(np.mean(average))
print(x_coords)
print(differences)
