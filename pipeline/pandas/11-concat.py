#!/usr/bin/env python3
"""Concatenate two DataFrames with labeled keys."""

import pandas as pd

index = __import__('10-index').index


def concat(df1, df2):
    """Concatenate Bitstamp and Coinbase DataFrames."""
    df1 = index(df1)
    df2 = index(df2)

    df2 = df2[df2.index <= 1417411920]

    return pd.concat([df2, df1], keys=["bitstamp", "coinbase"])
