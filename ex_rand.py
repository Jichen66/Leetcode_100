import numpy as np
def rand(a=0, b=1):
    return np.random.rand()*(b-a) + a
flip = rand()
print(flip)
