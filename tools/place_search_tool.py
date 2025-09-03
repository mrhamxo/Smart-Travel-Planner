import os
from utils.place_search import GooglePlaceSearchTool, TavilyPlaceSearchTool
from typing import List
from langchain.tools import tool
from dotenv import load_dotenv

class PlaceSearchTool:
    def __init__(self):
        # Load environment variables from .env file
        load_dotenv()
        
        # Fetch Google Places API key from environment
        self.google_api_key = os.environ.get("GPLACES_API_KEY")
        
        # Initialize Google and Tavily search helpers
        self.google_places_search = GooglePlaceSearchTool(self.google_api_key)
        self.tavily_search = TavilyPlaceSearchTool()
        
        # Setup LangChain-compatible tools
        self.place_search_tool_list = self._setup_tools()

    def _setup_tools(self) -> List:
        """Setup all tools for the place search tool"""

        @tool
        def search_attractions(place: str) -> str:
            """Search attractions of a place"""
            try:
                # Try fetching from Google Places
                attraction_result = self.google_places_search.google_search_attractions(place)
                if attraction_result:
                    return f"Following are the attractions of {place} as suggested by Google: {attraction_result}"
            except Exception as e:
                # Fallback to Tavily if Google fails
                tavily_result = self.tavily_search.tavily_search_attractions(place)
                return f"Google cannot find the details due to {e}. \nFollowing are the attractions of {place}: {tavily_result}"

        @tool
        def search_restaurants(place: str) -> str:
            """Search restaurants of a place"""
            try:
                restaurants_result = self.google_places_search.google_search_restaurants(place)
                if restaurants_result:
                    return f"Following are the restaurants of {place} as suggested by Google: {restaurants_result}"
            except Exception as e:
                # Fallback to Tavily if Google fails
                tavily_result = self.tavily_search.tavily_search_restaurants(place)
                return f"Google cannot find the details due to {e}. \nFollowing are the restaurants of {place}: {tavily_result}"

        @tool
        def search_activities(place: str) -> str:
            """Search activities of a place"""
            try:
                activities_result = self.google_places_search.google_search_activity(place)
                if activities_result:
                    return f"Following are the activities in and around {place} as suggested by Google: {activities_result}"
            except Exception as e:
                # Fallback to Tavily if Google fails
                tavily_result = self.tavily_search.tavily_search_activity(place)
                return f"Google cannot find the details due to {e}. \nFollowing are the activities of {place}: {tavily_result}"

        @tool
        def search_transportation(place: str) -> str:
            """Search transportation of a place"""
            try:
                transportation_result = self.google_places_search.google_search_transportation(place)
                if transportation_result:
                    return f"Following are the modes of transportation available in {place} as suggested by Google: {transportation_result}"
            except Exception as e:
                # Fallback to Tavily if Google fails
                tavily_result = self.tavily_search.tavily_search_transportation(place)
                return f"Google cannot find the details due to {e}. \nFollowing are the modes of transportation available in {place}: {tavily_result}"

        # Return list of all defined tools
        return [search_attractions, search_restaurants, search_activities, search_transportation]
