import os
import httpx
from dotenv import load_dotenv

load_dotenv()

def resolve_place(place_name: str, region: str = "IN") -> dict:
    """Resolve a place name to place_id, lat, lng, and label using Google Maps."""
    api_key = os.getenv("GOOGLE_MAPS_API_KEY")
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    resp = httpx.get(url, params={"address": place_name, "region": region, "key": api_key})
    data = resp.json()

    if data["status"] != "OK" or not data["results"]:
        return {"status": "error", "error_message": f"Could not resolve place: {place_name}"}

    result = data["results"][0]
    return {
        "status": "success",
        "place_id": result["place_id"],
        "label": result["formatted_address"],
        "lat": result["geometry"]["location"]["lat"],
        "lng": result["geometry"]["location"]["lng"],
    }