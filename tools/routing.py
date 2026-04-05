import os
import httpx
from typing import Dict, Any

def get_route(origin: str, destination: str) -> Dict[str, Any]:
    """
    Gets the real route between origin and destination using Google Maps Directions API.
    Returns distance, duration, and step-by-step directions.
    """
    api_key = os.getenv("GOOGLE_MAPS_API_KEY")
    url = "https://maps.googleapis.com/maps/api/directions/json"

    resp = httpx.get(url, params={
        "origin": origin,
        "destination": destination,
        "region": "IN",
        "key": api_key
    })
    data = resp.json()

    if data["status"] != "OK":
        return {"status": "error", "error_message": f"Could not get route: {data['status']}"}

    leg = data["routes"][0]["legs"][0]
    steps = [step["html_instructions"] for step in leg["steps"]]

    return {
        "status": "success",
        "origin": leg["start_address"],
        "destination": leg["end_address"],
        "distance": leg["distance"]["text"],
        "duration": leg["duration"]["text"],
        "steps": steps
    }