#!/usr/bin/env python3
"""Prepare and visualize daily Bitcoin data."""

import pandas as pd


def visualize(df):
    """Clean, aggregate, and plot Bitcoin data from 2017 onward."""
    df = df.drop(columns=["Weighted_Price"])
    df = df.rename(columns={"Timestamp": "Date"})
    df["Date"] = pd.to_datetime(df["Date"], unit="s")
    df = df.set_index("Date")
    df = df.sort_index()

    df["Close"] = df["Close"].ffill()

    for col in ["High", "Low", "Open"]:
        df[col] = df[col].fillna(df["Close"])

    df["Volume_(BTC)"] = df["Volume_(BTC)"].fillna(0)
    df["Volume_(Currency)"] = df["Volume_(Currency)"].fillna(0)

    df = df.loc["2017-01-01":]

    df = df.resample("D").agg({
        "High": "max",
        "Low": "min",
        "Open": "mean",
        "Close": "mean",
        "Volume_(BTC)": "sum",
        "Volume_(Currency)": "sum"
    })

    df.plot(subplots=True, figsize=(12, 12))

    return df
