#!/usr/bin/env python3
"""Fill missing values in a DataFrame."""


def fill(df):
    """Remove Weighted_Price and fill missing values."""
    df = df.drop(columns=["Weighted_Price"])
    df["Close"] = df["Close"].ffill()

    for col in ["High", "Low", "Open"]:
        df[col] = df[col].fillna(df["Close"])

    df["Volume_(BTC)"] = df["Volume_(BTC)"].fillna(0)
    df["Volume_(Currency)"] = df["Volume_(Currency)"].fillna(0)

    return df
