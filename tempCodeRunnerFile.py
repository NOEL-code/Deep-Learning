import numpy as np
import pandas as pd

def step_function(x):
    y = x > 0
    return y.astype(np.int)