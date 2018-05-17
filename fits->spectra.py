import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import astropy as asp
#import all relevant packages
from astropy.io import fits
#take out the fits files

spectrum = fits.open("/Users/zephan/Dropbox/SRMP_shared/IRTF-From-Daniel/FINISHMay26_RPM2012+6726.fits")
#go thru the path to have "spectrum" open the fits file
spectrum.info()
data = spectrum[0].data

df = pd.DataFrame()
df["Wavelength"] = data[0]
df["Flux"] = data[1]
df["FluxErr"] = data[2]

df1 = df[(df["Wavelength"]>=0.74)&(df["Wavelength"]<=2.4)]


plt.plot(df["Wavelength"], df["Flux"])


fig = plt.figure()
fig.set_size_inches(10, 6.45)
ax1 = fig.add_subplot(111)
for axis in ['top', 'bottom', 'left', 'right']: # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)
ax1.tick_params(axis = 'both', which = 'major', labelsize = 20, length = 8, width = 1.1)
ax1.tick_params(axis = 'both', which = 'major', labelsize = 20, length = 4, width = 1.1)
plt.yticks(fontsize = 20)

plt.plot(df1["Wavelength"], df1["Flux"], c="#005200")
plt.xlabel("Wavelength ($\mu m$)", fontsize = 25)
plt.ylabel('Flux ($erg\ s^{-1} cm^{-2} A^{-1}$', fontsize = 25)
#plt.title("Spectra of My L8", fontsize = 30)
plt.xlim(0.7, 2.6)
plt.ylim(-3*10**(-18), 5*10**(-17))


ax1.annotate('J', xy=(1.1275, 1*10**(-17)), fontsize=20, fontweight = "bold")
ax1.annotate('H', xy=(1.6, 1*10**(-17)), fontsize=20, fontweight = "bold")
ax1.annotate('K', xy=(2.1275, 1*10**(-17)), fontsize=20, fontweight = "bold")
ax1.annotate("2MASS J2012+6726",xy=(1.95,4.5*10**(-17)), fontsize=20)
ax1.annotate("Splat SpT:L8",xy=(1.95,4.20*10**(-17)), fontsize=20)
ax1.annotate("UTK SpT:L8",xy=(1.95,3.90*10**(-17)), fontsize=20)
plt.tight_layout()

plt.savefig("L8_Spectra.png", dpi=150)