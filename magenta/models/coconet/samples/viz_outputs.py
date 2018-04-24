import numpy as np
import matplotlib.pyplot as plt
import os
import sys

subdir = sys.argv[1]


res = np.load(os.path.join(subdir, 'generated_result.npy'))
#for i in range(len(res)):
pianoroll = res[0]
fig, ax = plt.subplots(nrows=2, ncols=2)
plt.suptitle('Final Pianorolls')
ctr = 0
for row in (ax):
	for col in row:
		col.imshow(pianoroll[:,:,ctr].T, cmap='Purples')
		ctr += 1
map(lambda a: a.set_aspect('auto'), ax.flatten())
plt.show()