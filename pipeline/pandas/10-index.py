#!/usr/bin/env python3
"""Set the Timestamp column as the DataFrame index."""


def index(df):
    """Return the DataFrame with Timestamp as its index."""
    return df.set_index("Timestamp")
