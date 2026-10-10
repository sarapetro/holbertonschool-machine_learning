#!/usr/bin/env python3
"""Load data from a file into a Pandas DataFrame."""

import pandas as pd


def from_file(filename, delimiter):
    """Load a file and return its contents as a DataFrame."""
    return pd.read_csv(filename, sep=delimiter)
