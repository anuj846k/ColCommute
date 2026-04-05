from google.adk.agents.llm_agent import Agent
from core.llm import MODEL_NAME
from tools.payment_processing import process_payment
from tools.feedback_logging_tool import log_feedback

after_ride_agent = Agent(             
    model=MODEL_NAME,
    name="after_ride_agent",
    description="Handles after-trip tasks: payment processing and feedback logging after a ride is completed.",
    tools=[process_payment, log_feedback],
    instruction="""
    You are the After-Ride Agent for the ColCommute system.
    
    Your responsibilities include:
    1. Processing Post-Ride Feedback: Analyze user feedback and ratings.
    2. Ride Logging: Mark the commute as completed.
    3. Payment Settlement: Trigger fare calculation and payment splitting among co-riders.
    4. Carbon Savings Calculation: Compute carbon footprint saved by carpooling.
    
    Only activate after a trip is fully confirmed and completed.
    """
)

