import numpy as np
from blimpy import Waterfall
import matplotlib
import matplotlib.pyplot as plt

print("Finished loading libraries.")

fname = '/Volumes/SETI_DATA/new_obs/2020-10-23-09:10:43/ics/ics_b.fil'

fb = Waterfall(fname, t_start = 0, t_stop = 1000)
data = fb.data.squeeze()

plt.imshow(data)
plt.savefig("img.png")