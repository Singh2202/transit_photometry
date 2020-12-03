
import glob
import lightkurve as lk
import numpy as np
import os
from keplersplinev2 import *
import matplotlib.pyplot as plt
import fnmatch
import math
for filename in glob.glob('*.txt'):
    if fnmatch.fnmatch(filename, "*24615*"):
        with open(os.path.join(os.getcwd(), filename), 'r') as f:
            data = np.genfromtxt(f, delimiter=',', usecols = [0,1], names=["time", "flux"], encoding = "Latin_1")
            data = np.delete(data, 0)
            lc = lk.LightCurve(data["time"], data["flux"])
            lc = lc.remove_nans()
            lc = lc.remove_outliers(sigma_upper=3)
            lc = lc.flatten()
            p = lc.to_periodogram('bls', duration=0.5)
            t0 = p.transit_time_at_max_power
            #period = p.period_at_max_power.value
            period = 13.1225
            lc = lc.fold(period)
            lc.to_csv(path_or_buf = "fmg.txt")
            #lc.scatter()

fluxes = []

with open("fmg.txt", 'r') as g:
    data = np.genfromtxt(g, delimiter=',', usecols = [1,2], names=["x", "y"], encoding = "Latin_1")
    data = np.delete(data, 0)
    quartiles = np.percentile(data["y"], [25, 50, 75])
    iqr = float(quartiles[2] - quartiles[0])
    outlier_threshold = float(1.5*iqr) + float(quartiles[1])
    new_fluxes = data[ (data["y"] <= outlier_threshold) ]
    time = [row[0] for row in new_fluxes]
    flux = [row[1] for row in new_fluxes]
    t = np.array(time)
    f = np.array(flux)
    lc = lk.LightCurve(time, flux)
    #lc.scatter()
    #print(y_values)
    #for thing in data["y"]:
        #if thing > outlier_threshold:
         #   new_fluxes = np.delete(data["y"], np.where(data["y"] == thing))
    #dif = len(data["y"]) - len(new_fluxes)
    #print(dif)
#print(len(fluxes))
#print(len(data["y"]))
     #lc = lk.LightCurve(data["x"], new_fluxes)
     
  #  lc = lc.remove_outliers(sigma_upper=3)
            #print(data["x"])
  #  lc.scatter(label = "yes");
  #  t = data["x"]
  #  f = data["y"]
           # print(min(f))
    import pandas as pd
    input_mask = np.ones_like(t, dtype=np.bool)
    input_mask[595:625] = False
    smasked, metadata = keplersplinev2(t, f, input_mask = input_mask, bkspace = 0.015, return_metadata=True)
    fig, ax = plt.subplots(figsize=(16, 8))
    #plt.plot(t, f,'.')
    #plt.plot(t, smasked,'o')
    df = pd.DataFrame(data=smasked)
    df.to_csv(path_or_buf = "/Users/sameersingh/desktop/joder/spline2.txt")
    
with open('spline2.txt', 'r') as g:
    data = np.genfromtxt(g, delimiter=',', usecols = [0,1], names=["x", "y"], encoding = "Latin_1")
    data = np.delete(data, 0)
    lc = lk.LightCurve(data["x"], data["y"])
    lc = lc.flatten()
    lc.to_csv(path_or_buf = "spline3.txt")

with open('spline3.txt', 'r') as g:
    data = np.genfromtxt(g, delimiter=',', usecols = [1,2], names=["x", "y"], encoding = "Latin_1")
    np.delete(data,0)
    ys = data["y"].tolist()
    ys = [x for x in ys if (math.isnan(x) is False)]
    xs = data["x"].tolist()
    xs = [x for x in xs if (math.isnan(x) is False)]
    minimum = min(ys)
    for x,y in data:
        if y == minimum:
            minimum_x = x
    upper_bound = float(minimum_x + float(max(xs)/10))
    lower_bound = float(minimum_x - float(max(xs)/10))
    newx = []
    for x in xs:
        if x > lower_bound and x < upper_bound:
            newx.append(x)
    start = int(min(newx)) - 1
    end = int(max(newx))
    newy = ys[start:end]
    zip(newx, newy)
    arr1 = np.array(newx)
    arr2 = np.array(newy)
    plt.scatter(arr1, arr2)
    import pwlf
    x = arr1
    y = arr2
    my_pwlf = pwlf.PiecewiseLinFit(x, y)
    breaks = my_pwlf.fit(2)
    x_hat = x
    y_hat = my_pwlf.predict(x)
    plt.figure()
    plt.plot(x, y, 'o')
    plt.plot(x_hat, y_hat, '-')
    plt.show()
    
    import csv
    with open('text5.csv', 'w') as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerows(zip(newx,newy))
        quit()
        
with open('text5.csv', 'r') as g:
    data = np.genfromtxt(g, delimiter=',', usecols = [0,1], names=["x", "y"], encoding = "Latin_1")     
    lc = lk.LightCurve(data['x'], data['y'])
    lc.scatter(label = "test")
    slopes = []
    deltax = []
    for x in zip(data, data[1:]):
        delx = (x[1][0]-x[0][0])
        slope = (x[1][1]-x[0][1])/(x[1][0]-x[0][0])
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
        end2 = len(sq)
        x_vals = list(range(0, end2))
        y_vals = sq
        #plt.scatter(x_vals, y_vals)
        s = pd.Series(y_vals)
        a = s.rolling(5).median()
        #print(tyo)
        ##from scipy import optimize
        #x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11, 12, 13, 14, 15], dtype=float)
        #y = np.array([5, 7, 9, 11, 13, 15, 28.92, 42.81, 56.7, 70.59, 84.47, 98.36, 112.25, 126.14, 140.03])
##def piecewise_linear(x, x0, y0, k1, k2):
     #       return np.piecewise(x, [x < x0], [lambda x:k1*x + y0-k1*x0, lambda x:k2*x + y0-k2*x0])
     #   p , e = optimize.curve_fit(piecewise_linear, x, y)
      #  xd = np.linspace(0, 15, 100)
      #  plt.plot(x, y, "o")
      #  plt.plot(xd, piecewise_linear(xd, *p))


    
        # df = pd.DataFrame(data=smasked)
        # df.to_csv(path_or_buf = "/Volumes/ExtremeSSD/xt.csv")
        ## print(metadata.bkspace)
        # lc.scatter(label = "EPIC" + str(filename));
