from typing import Dict, Any

def log_feedback(ride_id: str, user_id: str, feedback_score: int, feedback_text: str) -> Dict[str, Any]:
    """
    Logs user feedback for a completed ride.
    """
    if not 1 <= feedback_score <= 5:
        return {"status": "error", "message": "feedback_score must be between 1 and 5."}

    return {
        "status": "success",
        "message": f"Feedback for ride {ride_id} has been logged successfully.",
        "feedback_id": "feedback_12345"  # replace with real DB write in production
    }

log_feedback_tool = log_feedback