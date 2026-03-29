import requests
import os

GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

#  Hardcoded coordinates (no geocoding needed)
def get_coordinates(location: str):
    mapping = {
        "Mumbai": (19.0760, 72.8777),
        "Thane": (19.2183, 72.9781),
        "Bandra": (19.0596, 72.8295)
    }
    return mapping.get(location, (19.0760, 72.8777))  # default Mumbai


def get_nearby_places(location: str, place_type: str):
    lat, lng = get_coordinates(location)

    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

    params = {
        "location": f"{lat},{lng}",
        "radius": 3000,
        "type": place_type,
        "key": GOOGLE_MAPS_API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data.get("status") != "OK":
        print("MAP ERROR:", data)
        return {
            "location": location,
            "type": place_type,
            "places": [],
            "error": data.get("status")
        }

    results = []

    for place in data.get("results", [])[:5]:
        results.append({
            "name": place.get("name"),
            "rating": place.get("rating", 0),
            "address": place.get("vicinity")
        })

    return {
        "location": location,
        "type": place_type,
        "places": results
    }
