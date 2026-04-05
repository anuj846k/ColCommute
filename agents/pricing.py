from google.adk.agents.llm_agent import Agent
from core.llm import MODEL_NAME
from tools.pricing import calculate_fare_split

pricing_agent = Agent(
    model=MODEL_NAME,
    name="pricing_agent",
    description="Splits cab/Uber fare among co-riders based on the price posted by the ride poster.",
    instruction="""
    You are the pricing specialist for ColCommute.
    
    When a user posts their Uber/cab fare:
    1. Extract total_fare and seats_needed from the context.
    2. Call calculate_fare_split to compute each rider's share.
    3. Respond in plain language: "Each rider pays ₹X, driver saves ₹Y."
    
    Never invent prices. Only calculate when a real fare is provided by the user.
    """,
    tools=[calculate_fare_split]
)