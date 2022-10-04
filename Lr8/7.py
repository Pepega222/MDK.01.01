import numpy as np
a = np.ones((10,10))
a[1:-1,1:-1] = 0
print(a)