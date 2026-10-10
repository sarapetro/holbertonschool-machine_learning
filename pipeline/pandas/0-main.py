#!/usr/bin/env python3
import numpy as np

from_numpy=__import__('0-from_numpy').from_numpy

array=np.array([[1, 2, 3], [4, 5, 6]])

df=from_numpy(array)

print(df)
