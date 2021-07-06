import numpy as np
from blimpy import Waterfall
import matplotlib
import matplotlib.pyplot as plt
import time

print("Finished loading libraries.")

JUMP_MAG_TOLERANCE = 1 #(raw value. values in the bandpass and timeseries will range from 0 to 255)

start = time.time()

fname = '/mnt/datay-netStorage-40G/new_obs/2021-06-26-17:52:42/ics/ics.fil'

fb = Waterfall(fname, t_start = 160000, t_stop = 180000)
data = fb.data.squeeze()

#plt.imshow(data)
#plt.savefig("img.png")
np.save("origarr.npy", data)

bp = data.mean(axis = 0)
bp_med = np.median(bp)
exceeds = np.where(np.abs(bp - bp_med) > JUMP_MAG_TOLERANCE)

newdata = data
newdata[:, exceeds] = bp_med

np.save("newarr.npy", newdata)

print(time.time() - start)
