#!/usr/bin/env python3
"""Find Star Wars starships by passenger capacity."""

import requests


BASE_URL = "https://swapi-api.hbtn.io/api/starships/"


def availableShips(passengerCount):
    """Return ships that can hold at least passengerCount passengers."""
    ships = []
    url = BASE_URL

    while url:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        for ship in data["results"]:
            passengers = ship["passengers"].replace(",", "")

            if passengers.isdigit():
                if int(passengers) >= passengerCount:
                    ships.append(ship["name"])

        url = data["next"]

    return ships
