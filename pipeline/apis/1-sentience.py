#!/usr/bin/env python3
"""Find the home planets of sentient Star Wars species."""

import requests


BASE_URL = "https://swapi-api.hbtn.io/api/species/"


def sentientPlanets():
    """Return home planet names for all sentient species, across all pages."""
    planets = []
    url = BASE_URL

    while url:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        for species in data["results"]:
            if (species["classification"].lower() == "sentient" or
                    species["designation"].lower() == "sentient"):
                homeworld = species["homeworld"]
                if homeworld:
                    planet_response = requests.get(homeworld, timeout=10)
                    planet_response.raise_for_status()
                    planets.append(planet_response.json()["name"])

        url = data["next"]

    return planets
