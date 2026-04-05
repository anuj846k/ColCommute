from __future__ import annotations
from typing import Optional
from services import ride_services as rs
from tools.geocode import resolve_place


def register_commute_post(
    user_id: str,
    origin: str,
    destination: str,
    time_bucket: str,
    vacant_seats: int = 0,
    seats_needed: int = 0,
    destination_place_id: Optional[str] = None,
    destination_lat: Optional[float] = None,
    destination_lng: Optional[float] = None,
    destination_label: Optional[str] = None,
    origin_place_id: Optional[str] = None,
    origin_lat: Optional[float] = None,
    origin_lng: Optional[float] = None,
    origin_label: Optional[str] = None,
) -> dict:
    """
    Register one commute post. Origin and destination can be plain place names —
    coordinates and place_id are resolved automatically via geocoding.
    """
    # Auto-resolve destination
    if not destination_place_id or destination_lat is None or destination_lng is None:
        geo = resolve_place(destination)
        if geo["status"] != "success":
            return {"status": "error", "error_message": f"Could not resolve destination: {destination}"}
        destination_place_id = geo["place_id"]
        destination_lat = geo["lat"]
        destination_lng = geo["lng"]
        destination_label = destination_label or geo["label"]

    # Auto-resolve origin (non-fatal if it fails)
    if not origin_place_id or origin_lat is None or origin_lng is None:
        geo = resolve_place(origin)
        if geo["status"] == "success":
            origin_place_id = geo["place_id"]
            origin_lat = geo["lat"]
            origin_lng = geo["lng"]
            origin_label = origin_label or geo["label"]

    return rs.register_commute_post(
        user_id=user_id,
        origin=origin,
        destination=destination,
        destination_place_id=destination_place_id,
        destination_lat=destination_lat,
        destination_lng=destination_lng,
        destination_label=destination_label,
        time_bucket=time_bucket,
        vacant_seats=vacant_seats,
        seats_needed=seats_needed,
        origin_place_id=origin_place_id,
        origin_lat=origin_lat,
        origin_lng=origin_lng,
        origin_label=origin_label,
    )


def find_matches_for_commute_post(commute_post_id: str) -> dict:
    """Find compatible commute posts for this commute_post_id (offer paired with need)."""
    return rs.find_matches_for_commute_post(commute_post_id)


def list_commute_posts(destination_substring: Optional[str] = None) -> dict:
    """List registered commute posts; filter by destination substring if provided."""
    return rs.list_commute_posts(destination_substring=destination_substring)


def confirm_trip(offer_commute_post_id: str, need_commute_post_id: str) -> dict:
    """
    Record a finalized trip after mutual agreement: offer post UUID, then need post UUID.

    Production should require verified consent from both users; this call only enforces
    data rules, not real-world agreement.
    """
    return rs.confirm_trip(offer_commute_post_id, need_commute_post_id)

def register_user(user_id: str) -> dict:
    """Register a new user in the system if they don't exist yet."""
    return rs.register_user(user_id=user_id)