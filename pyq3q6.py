import numpy as np
import random
ones_array = np.ones(200)
zeros_array = np.zeros(100)
sixes_array = np.full(180,60)

combined_array = np.concatenate((ones_array, zeros_array, sixes_array))

random.shuffle(combined_array)

reshaped_array = np.reshape(combined_array, (8, 60))
print(reshaped_array)
