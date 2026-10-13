#!/usr/bin/env python3
"""Remove rows with missing Close values from a DataFrame."""


def prune(df):
    """Return the DataFrame without rows containing NaN in Close."""
    return df.dropna(subset=["Close"])
