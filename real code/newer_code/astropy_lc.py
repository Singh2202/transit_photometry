import os
import pandas as pd
import lightkurve as lk
import itertools
import warnings
jd_times = []
fluxes = []
warnings.filterwarnings("ignore")
for file in os.listdir("/Users/sameersingh/.lightkurve-cache/mastDownload/Kepler/kplr006850504_lc_Q011111111111111111"):
    from astropy.timeseries import TimeSeries
    file = os.path.join("/Users/sameersingh/.lightkurve-cache/mastDownload/Kepler/kplr006850504_lc_Q011111111111111111", file)
    ts = TimeSeries.read(file, format='kepler.fits') 
    times = ts.time.jd
    jd_times.append(times)
    df  = ts.to_pandas()
    pdcsap = (df["pdcsap_flux"])
    lc = lk.LightCurve(times, pdcsap).normalize()
    fluxes.append(lc.flux)
jd_times = list(itertools.chain(*jd_times))
fluxes = list(itertools.chain(*fluxes))
lc.scatter(jd_times, fluxes)
