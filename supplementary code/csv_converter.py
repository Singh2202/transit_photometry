import os
import pandas as pd 
empty = []
for filename in os.listdir("/Volumes/ExtremeSSD/Files"):
    if filename.endswith(".txt"): 
        empty.append(os.path.join("/Volumes/ExtremeSSD/Files", filename))

    
counter = 0
for name in empty:
    df = pd.read_csv(str(name), delimiter=',')
    counter = counter + 1
    df.to_csv('kepler' + str(counter) + 'k.csv')
