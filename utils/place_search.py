import os
import json
from langchain_tavily import TavilySearch
from langchain_google_community import GooglePlacesTool, GooglePlacesAPIWrapper 

# -------------------------
# Google Places Search Tool
# -------------------------
class GooglePlaceSearchTool:
    def __init__(self, api_key: str):
        # Initialize Google Places API wrapper with the provided API key
        self.places_wrapper = GooglePlacesAPIWrapper(gplaces_api_key=api_key)
        
        # Create Google Places tool using the wrapper
        self.places_tool = GooglePlacesTool(api_wrapper=self.places_wrapper)
    
    def google_search_attractions(self, place: str) -> dict:
        
        """Searches for attractions in the specified place using Google Places API."""
        return self.places_tool.run(f"top attractive places in and around {place}")
    
    def google_search_restaurants(self, place: str) -> dict:
        
        """Searches for available restaurants in the specified place using Google Places API."""
        return self.places_tool.run(f"what are the top 10 restaurants and eateries in and around {place}?")
    
    def google_search_activity(self, place: str) -> dict:
        
        """Searches for popular activities in the specified place using Google Places API."""
        return self.places_tool.run(f"Activities in and around {place}")

    def google_search_transportation(self, place: str) -> dict:
        
        """Searches for available modes of transportation in the specified place using Google Places API."""
        return self.places_tool.run(f"What are the different modes of transportations available in {place}")


# -------------------------
# Tavily Place Search Tool
# -------------------------
class TavilyPlaceSearchTool:
    def __init__(self):
        pass

    def tavily_search_attractions(self, place: str) -> dict:
        
        """Searches for attractions in the specified place using TavilySearch."""
        
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"top attractive places in and around {place}"})
        
        return result.get("answer") if isinstance(result, dict) and result.get("answer") else result
    
    def tavily_search_restaurants(self, place: str) -> dict:
        
        """Searches for available restaurants in the specified place using TavilySearch."""
        
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"what are the top 10 restaurants and eateries in and around {place}."})
        
        return result.get("answer") if isinstance(result, dict) and result.get("answer") else result
    
    def tavily_search_activity(self, place: str) -> dict:
        
        """Searches for popular activities in the specified place using TavilySearch."""
        
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"activities in and around {place}"})
        
        return result.get("answer") if isinstance(result, dict) and result.get("answer") else result

    def tavily_search_transportation(self, place: str) -> dict:
        
        """Searches for available modes of transportation in the specified place using TavilySearch."""
        
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"What are the different modes of transportations available in {place}"})
        
        return result.get("answer") if isinstance(result, dict) and result.get("answer") else result
