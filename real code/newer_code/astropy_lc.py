jd_times = []
fluxes = []
import os
import matplotlib.pyplot as plt
import pandas as pd
import lightkurve as lk
length = 0
for file in os.listdir("/Users/sameersingh/.lightkurve-cache/mastDownload/Kepler/kplr006850504_lc_Q011111111111111111"):
    from astropy.timeseries import TimeSeries
    file = os.path.join("/Users/sameersingh/.lightkurve-cache/mastDownload/Kepler/kplr006850504_lc_Q011111111111111111", file)
    ts = TimeSeries.read(file, format='kepler.fits') 
    times = ts.time.jd
    jd_times.append(times)
    df  = ts.to_pandas()
    pdcsap = (df["pdcsap_flux"])
    for value in pdcsap:
        fluxes.append(value)

import itertools
jd_times = list(itertools.chain(*jd_times))
