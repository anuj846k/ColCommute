from google.adk.agents.llm_agent import Agent
from agents.routing import routing_agent
from agents.pricing import pricing_agent
from core.llm import get_model_config
from agents.ride_matching import ride_matching_agent
from agents.ride import after_ride_agent

orchestrator: Agent = Agent(
    model=get_model_config(),
    name="commute_orchestrator",
    description="Coordinates ride matching, routing, pricing for student commute",

    sub_agents=[
        ride_matching_agent,
        routing_agent,
        pricing_agent,
        after_ride_agent,
    ],

    instruction="""
    You are the Commute Orchestrator. Your goal is to coordinate the full student commute lifecycle:
    
    1. **Matching**: Call ride_matching_agent to register and find carpool partners.
    2. **Routing**: Use routing_agent to get real distance and duration.
    3. **Pricing**: Use pricing_agent to split the fare when the user provides their Uber price.
    4. **Completion**: Use after_ride_agent for payments and feedback after the ride.
    
    Orchestration Flow:
    Request -> Matching -> Routing -> Pricing -> After-Ride.

    ## Strict routing rules
    - "post a ride", "I want to commute", "I have seats" → ONLY ride_matching_agent.
    - Pricing is only calculated when the user explicitly provides a fare amount.
    - after_ride_agent is ONLY called after a trip is fully completed.
    """,
)