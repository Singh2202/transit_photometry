
import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline              
detection_method = [' Astrometry ', 'Imaging', 'Radial Velocity', 'Transit', 'Transit timing variations', 'Eclipse timing variations', 'Microlensing', 'Pulsar timing variations', 'Pulsation timing variations', 'Orbital brightness variations', 'Disk Kinematics']
l = [1, 51, 820, 3253, 21, 16, 98, 7, 2, 6, 1]
total = 0
for thing in range(0, len(l)): 
    total = total + l[thing]
new = []
for thing in l:
    b = (thing/total*100)
    new.append(b)
    
for m in new:
    print(m)
    
ypos = np.arange(len(detection_method))
plt.xticks(ypos, detection_method)
plt.title("Percentage of Known Exoplanets Discovered by Each Technique")
plt.ylabel("Percentage of Known Exoplanets")
plt.xlabel("Detection Method")
plt.xticks(rotation = 90)
plt.bar(ypos, new)
