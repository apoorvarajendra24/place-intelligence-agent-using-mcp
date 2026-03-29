from fastapi import FastAPI
from tools import get_nearby_places

app = FastAPI()

@app.get("/")
def root():
    return {"message": "MCP Server Running"}

# MCP-style tool endpoint
@app.post("/tools/get_nearby_places")
def nearby_places_tool(payload: dict):
    print(f"MCP CALLED WITH: {payload}")
    
    location = payload.get("location")
    place_type = payload.get("place_type", "cafe") # Default to cafe

    # Call your tool function
    result = get_nearby_places(location, place_type=place_type)

    # Return the list directly so the LLM can "see" it easily
    return result
