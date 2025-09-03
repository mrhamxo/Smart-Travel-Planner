import os
from langchain.tools import tool
from typing import List
from dotenv import load_dotenv
from utils.weather_info import WeatherForecastTool

class WeatherInfoTool:
    """
    WeatherInfoTool provides methods to fetch real-time weather data and weather forecasts for a given city.
    
    Attributes:
        api_key (str): The API key for accessing the weather service, loaded from environment variables.
        weather_service (WeatherForecastTool): An instance of the weather service client.
        weather_tool_list (list): A list of weather-related tools (functions) set up for use.
    
    Methods:
        _setup_tool() -> list:
            Defines and returns a list of weather-related tool functions:
                - get_current_weather(city: str) -> str: Fetches and returns the current weather.
                - get_weather_forecast(city: str) -> str: Fetches and returns the weather forecast.
    """
    
    def __init__(self):
        """
        Initialize the WeatherInfoTool.
        - Load API key from environment variables.
        - Initialize the weather service client.
        - Register weather tools (current weather and forecast).
        """
        load_dotenv()  # Load environment variables from .env file
        self.api_key = os.environ.get("OPENWEATHERMAP_API_KEY")  # Get API key safely
        self.weather_service = WeatherForecastTool(self.api_key)  # Weather service instance
        
        # NOTE: Your method is named `_setup_tool`, but here you're calling `_setup_tools`
        # This will raise an AttributeError. Fix by renaming consistently.
        self.weather_tool_list = self._setup_tool()
    
    def _setup_tool(self) -> list:
        """
        Initializes and returns a list of weather-related tool functions.
        Defines and registers:
            1. get_current_weather(city: str) -> str
            2. get_weather_forecast(city: str) -> str
        Returns:
            list: A list of tool functions.
        """

        @tool
        def get_current_weather(city: str) -> str:
            """
            Fetches real-time weather data for a given city.
            Args:
                city (str): Name of the city.
            Returns:
                str: Current temperature and description, or error message.
            """
            # Fetch weather from service
            weather_data = self.weather_service.get_current_weather(city)
            
            if weather_data:
                temp = weather_data.get('main', {}).get('temp', 'N/A')
                desc = weather_data.get('weather', [{}])[0].get('description', 'N/A')
                return f"Current weather in {city}: {temp}°C, {desc}"
            
            return f"Could not fetch weather for {city}"
        
        @tool
        def get_weather_forecast(city: str) -> str:
            """
            Retrieves the weather forecast for a city.
            Args:
                city (str): City name.
            Returns:
                str: Forecast summary or error message.
            """
            forecast_data = self.weather_service.get_forecast_weather(city)
            
            # Check if forecast data is valid
            if forecast_data and 'list' in forecast_data:
                forecast_summary = []
                
                # Loop through forecast list (3-hour intervals usually)
                for i in range(len(forecast_data['list'])):
                    item = forecast_data['list'][i]
                    date = item['dt_txt'].split(' ')[0]
                    temp = item['main']['temp']
                    desc = item['weather'][0]['description']
                    
                    # Append formatted forecast string
                    forecast_summary.append(f"{date}: {temp}°C, {desc}")
                    
                return f"Weather forecast for {city}:\n" + "\n".join(forecast_summary)
            
            return f"Could not fetch forecast for {city}"
    
        # Return both tools as a list
        return [get_current_weather, get_weather_forecast]