
# Probability

This project introduces probability distributions using Python.

## Tasks

### 0. Initialize Poisson
Create a `Poisson` class that represents a Poisson distribution.

- Initialize the distribution using `lambtha` or a list of data.
- Calculate `lambtha` from the provided data.
- Validate the input data.

### 1. Poisson PMF
Implement the `pmf` method to calculate the Probability Mass Function (PMF).

- Convert `k` to an integer if necessary.
- Return `0` if `k` is out of range.
- Calculate the probability using the Poisson formula.

## Mathematical Formula

The Poisson Probability Mass Function is:

P(X = k) = (e^(-λ) * λ^k) / k!

Where:
- `λ` is the expected number of occurrences.
- `k` is the number of occurrences.
- `e` is Euler's number.
- `k!` is the factorial of `k`.

