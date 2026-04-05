from typing import Dict, Any

def calculate_fare_split(total_fare: float, seats_needed: int) -> Dict[str, Any]:
    """
    Splits the total Uber/cab fare among riders.
    total_fare: the price the ride poster paid or expects.
    seats_needed: number of co-riders splitting the fare.
    """
    if seats_needed <= 0:
        return {"status": "error", "error_message": "seats_needed must be at least 1."}
    if total_fare <= 0:
        return {"status": "error", "error_message": "total_fare must be greater than 0."}

    rider_share = round(total_fare / (seats_needed + 1), 2)
    driver_share = round(total_fare - (rider_share * seats_needed), 2)

    return {
        "status": "success",
        "total_fare": total_fare,
        "seats_needed": seats_needed,
        "per_rider_share": rider_share,
        "driver_share": driver_share,
        "summary": f"Total ₹{total_fare} split: each rider pays ₹{rider_share}, driver saves ₹{driver_share}"
    }