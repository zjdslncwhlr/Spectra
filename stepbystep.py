import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import astropy as asp
from astropy.io import fits
#take out fits stuff

spectrum = fits.open("/Users/zephan/Dropbox/SRMP_shared/IRTF-From-Daniel/FINISHMay26_RPM2012+6726.fits")
#open the fits file and call it a name, for the file path drag the file to terminal to see its path

spectrum.info()
#look at the fits file info

data = spectrum[0].data
#There are three pieces of info, the flux, the wavelength, flux range

df = pd.DataFrame()
#