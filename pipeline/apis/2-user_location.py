#!/usr/bin/env python3
"""Print a GitHub user's location and handle API rate limits."""

import sys
import time

import requests


def main():
    """Fetch the user API URL passed as the first command-line argument."""
    response = requests.get(sys.argv[1], timeout=10)

    if response.status_code == 404:
        print("Not found")
    elif response.status_code == 403:
        reset = int(response.headers["X-RateLimit-Reset"])
        minutes = max(0, int((reset - time.time()) / 60))
        print("Reset in {} min".format(minutes))
    else:
        response.raise_for_status()
        print(response.json().get("location"))


if __name__ == '__main__':
    main()
