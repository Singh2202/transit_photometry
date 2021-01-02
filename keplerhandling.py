import fnmatch
import os
from astropy.timeseries import TimeSeries
import lightkurve as lk
import pandas as pd
import itertools

parent_directory = "/Users/sameersingh/.lightkurve-cache/mastDownload/Kepler"
all_times = [[] for x in range(len(fnmatch.filter(os.listdir(parent_directory), 'kplr*')))]
all_fluxes = [[] for x in range(len(fnmatch.filter(os.listdir(parent_directory), 'kplr*')))]
list_of_kepler_ids = []

for subdirectory in os.listdir(parent_directory):
    if fnmatch.fnmatch(subdirectory, "kplr*"):
        list_of_kepler_ids.append(subdirectory[:13])
        jd_times = []
        fluxes = []
        for file in os.listdir(os.path.join(parent_directory, subdirectory)):
            file = os.path.join(parent_directory, subdirectory, file)
            ts = TimeSeries.read(file, format='kepler.fits') 
            times = ts.time.jd
            df = ts.to_pandas()
            pdcsap = (df["pdcsap_flux"])
            lc = lk.LightCurve(times, pdcsap).normalize()
            lc = lc.remove_nans()
            fluxes.append(lc.flux)
            jd_times.append(lc.time)
        jd_times = list(itertools.chain(*jd_times))
        fluxes = list(itertools.chain(*fluxes))
    all_times.append(jd_times)
    all_fluxes.append(fluxes)
    
all_times.sort()    
all_fluxes.sort()
all_times = list(all_times for all_times,_ in itertools.groupby(all_times))
all_fluxes = list(all_fluxes for all_fluxes,_ in itertools.groupby(all_fluxes))

for element in all_times:
    if len(element) == 0:
        all_times.remove(element)
        
for element in all_fluxes:
    if len(element) == 0:
        all_fluxes.remove(element)

for i in range(len(all_times)):
    lc = lk.LightCurve(all_times[i], all_fluxes[i])
    lc.scatter();
