#!/usr/bin/env python3
"""Defines a binomial distribution class."""


class Binomial:
    """Represents a binomial distribution."""

    def __init__(self, data=None, n=1, p=0.5):
        """Initialize a binomial distribution from data or given parameters."""
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(n)
            self.p = float(p)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            mean = sum(data) / len(data)
            variance = sum((x - mean) ** 2 for x in data) / len(data)
            p = 1 - variance / mean
            self.n = round(mean / p)
            self.p = float(mean / self.n)

    def pmf(self, k):
        """Calculate the PMF for a given number of successes."""
        if not isinstance(k, int):
            k = int(k)

        if k < 0 or k > self.n:
            return 0

        combination = 1
        for i in range(1, min(k, self.n - k) + 1):
            combination = combination * (self.n - i + 1) // i

        return (combination * self.p ** k *
                (1 - self.p) ** (self.n - k))

    def cdf(self, k):
        """Calculate the CDF for a given number of successes."""
        if not isinstance(k, int):
            k = int(k)

        if k < 0 or k > self.n:
            return 0

        probability = 0
        for i in range(k + 1):
            probability += self.pmf(i)

        return probability
