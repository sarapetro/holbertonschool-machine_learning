#!/usr/bin/env python3
"""Defines a normal distribution class."""


class Normal:
    """Represents a normal distribution."""

    def __init__(self, data=None, mean=0., stddev=1.):
        """Initialize a normal distribution from data or given parameters."""
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            self.mean = float(sum(data) / len(data))
            variance = sum((x - self.mean) ** 2 for x in data) / len(data)
            self.stddev = float(variance ** 0.5)

    def z_score(self, x):
        """Calculate the z-score for a given x-value."""
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """Calculate the x-value for a given z-score."""
        return self.mean + z * self.stddev

    def pdf(self, x):
        """Calculate the PDF for a given x-value."""
        e = 2.7182818285
        pi = 3.1415926536
        z = self.z_score(x)
        return e ** (-0.5 * z ** 2) / (self.stddev * (2 * pi) ** 0.5)
