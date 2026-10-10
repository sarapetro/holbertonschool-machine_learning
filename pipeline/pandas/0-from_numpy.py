#!/usr/bin/env python3
"""Convert a NumPy array into a DataFrame"""

import pandas as pd

def from_numpy(array):
    """Create a DataFrame with alphabetically labeled columns."""
    columns=[chr(65+i) for i in range(array.shape[1])]
    return pd.DataFrame(array, columns=columns)