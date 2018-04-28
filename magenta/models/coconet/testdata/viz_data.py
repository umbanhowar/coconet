from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt


fname = 'LPDTest.npz'
f = np.load(fname)

songs = f['train']
song = np.random.choice(len(songs))
print('Song index:', song)
inst = np.random.choice(4)
print('Inst:', inst)

plt.imshow(songs[song][:,:,inst].T)
plt.axes().set_aspect('auto')
plt.show()