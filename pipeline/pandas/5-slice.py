#!/usr/bin/env python3
"""Slice a DataFrame by selecting specific columns and rows."""


def slice(df):
    """Return every 60th row of the selected DataFrame columns."""
    return df[["High", "Low", "Close", "Volume_(BTC)"]].iloc[::60]
