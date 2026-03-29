import os
from google.adk.agents import Agent
from .tools import get_nearby_places


# Tool wrapper for ADK
def nearby_places_tool(location: str, place_type: str):
    return get_nearby_places(location, place_type)

# Create ADK Agent
root_agent = Agent(
    name="place_intelligence_agent",
    model=os.getenv("MODEL", "gemini-2.5-flash"),
    description="Analyzes places using Google Maps",
    tools=[nearby_places_tool],
    instruction="""
    You are a Place Intelligence Agent.

    MANDATORY:
    - ALWAYS call the tool for ANY location query
    - NEVER answer without using the tool

    You MUST extract:
    - location
    - place_type

    Mappings:
    - "eat" → restaurant
    - "food" → restaurant
    - "study" → cafe
    - "hangout" → cafe

    Return results clearly with names and ratings.
    """
)

if __name__ == "__main__":
    print("Agent ready")
