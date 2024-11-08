import numpy as np
import matplotlib.pyplot as plt

array = np.ones((8,8))

array[1:-1, 1:-1] = 0

plt.imshow(array, cmap='gray', interpolation = 'nearest')
plt.colorbar(label='Value')

plt.title("8x8 Frame Array")
plt.savefig('frame_plot.png')
plt.close()
#plt.show()