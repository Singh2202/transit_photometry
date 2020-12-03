
  
import glob
import fnmatch
import os
import numpy as np
import pandas as pd
import lightkurve as lk
from keplersplinev2 import *
import itertools
import csv
for filename in glob.glob('*.txt'):
    if fnmatch.fnmatch(filename, "*20608*"):
        with open(os.path.join(os.getcwd(), filename), 'r') as f:
            data = np.genfromtxt(f, delimiter=',', usecols = [0,1], names=["time", "flux"], encoding = "Latin_1")
            data = np.delete(data, 0)
            input_mask = np.ones_like(data["time"], dtype=np.bool)
            input_mask[595:625] = False
            s, metadata = choosekeplersplinev2(data["time"], data["flux"], return_metadata=True)
            flatten_lc = list(data["flux"]/s)
            x_coords = list(data["time"])
            xy = [x for x in itertools.chain.from_iterable(itertools.zip_longest(x_coords,flatten_lc)) if x]
            coords = [xy[x:x + 2] for x in range(0, len(xy), 2)] 
            x_coords2 = [row[0] for row in coords]
            y_coords = [row[1] for row in coords]
            quartiles = np.percentile(y_coords, [25, 50, 75])
            iqr = float(quartiles[2] - quartiles[0])
            outlier_threshold = float(1.5*iqr) + float(quartiles[1])
            new_y_coords = [ flux for flux in y_coords if flux <= outlier_threshold] 
            good_times = []
            for x, y in coords:
                if y in new_y_coords:
                    good_times.append(x)
            xy2 = [x for x in itertools.chain.from_iterable(itertools.zip_longest(good_times,new_y_coords)) if x]
            coords2 = [xy2[x:x + 2] for x in range(0, len(xy2), 2)] 
            x_coords_final = [row[0] for row in coords2]
            y_coords_final = [row[1] for row in coords2]
            fig, ax = plt.subplots(figsize=(8, 4))
            plt.scatter(x_coords_final,y_coords_final)
