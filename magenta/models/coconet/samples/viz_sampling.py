import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os
import sys
import re

subdir = sys.argv[1]

steps = np.load(os.path.join(subdir, 'intermediate_steps.npz'))

num_search = re.compile(r'(\d+)_independent_sampler')
tipe_search = re.compile(r'(masks|predictions|pianorolls)')

inst = 0
batch = 0

masks = []
predictions = []
pianorolls = []
for f in steps.files:
	arr = steps[f][batch, :, :, inst]
	num_match = num_search.search(f)
	try:
		num = int(num_match.group(1))
	except AttributeError:
		# There are a few that look like 0_root/0_igibbs_strategy/0_gibbs_sampler/1_masks
		continue
	tipe_match = tipe_search.search(f)
	tipe = tipe_match.group(0)
	if tipe == 'masks':
		masks.append((num, arr))
	elif tipe == 'predictions':
		predictions.append((num, arr))
	elif tipe == 'pianorolls':
		pianorolls.append((num, arr))
	else:
		raise Exception

masks.sort(key=lambda x: x[0])
predictions.sort(key=lambda x: x[0])
pianorolls.sort(key=lambda x: x[0])

masks_arr = np.stack(map(lambda x: x[1], masks))
predictions_arr = np.stack(map(lambda x: x[1], predictions))
pianorolls_arr = np.stack(map(lambda x: x[1], pianorolls))

ims = [None, None, None]

idx = 0

fig, ax = plt.subplots(3, 1)

ims[0] = ax[0].imshow(masks_arr[idx, :, :].T, cmap='Purples')
ims[1] = ax[1].imshow(predictions_arr[idx, :, :].T, cmap='Purples')
ims[2] = ax[2].imshow(pianorolls_arr[idx, :, :].T, cmap='Purples')

map(lambda a: a.set_aspect('auto'), ax)

def updatefig(*args):
	global idx
	idx = (idx + 1) % len(masks_arr)
	ims[0].set_array(masks_arr[idx, :, :].T)
	ims[1].set_array(predictions_arr[idx, :, :].T)
	ims[2].set_array(pianorolls_arr[idx, :, :].T)
	return ims

ani = animation.FuncAnimation(fig, updatefig, interval=250, blit=True)

plt.show()

# def updatefig(*args):
# 	global idx
# 	idx = (idx + 1) % len(predictions_arr)
# 	im.set_array(predictions_arr[idx, :, :])
# 	return im,

# ani = animation.FuncAnimation(fig, updatefig, interval=150, blit=True)
# plt.show(block=False)

# fig2 = plt.figure()

# idx2 = 0
# im2 = plt.imshow(mask_arr[idx2, :, :])

# def updatefig2(*args):
# 	global idx2
# 	idx2 = (idx2 + 1) % len(mask_arr)
# 	im2.set_array(mask_arr[idx2, :, :])
# 	return im2,

# ani2 = animation.FuncAnimation(fig2, updatefig2, interval=150, blit=True)
# plt.show()

