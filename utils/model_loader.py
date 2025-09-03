from dotenv import load_dotenv
from typing import Literal, Optional, Any
from pydantic import BaseModel, Field
from utils.config_loader import load_config   # custom function to load YAML config
from langchain_groq import ChatGroq           # LangChain wrapper for Groq LLMs
from langchain_openai import ChatOpenAI       # LangChain wrapper for OpenAI LLMs
import os

load_dotenv()  # Load environment variables from .env file

# ------------------------------
# Config Loader Class
# ------------------------------
class ConfigLoader:
    """
    This class loads the project configuration from config.yaml
    using the custom `load_config()` function.
    It also allows dictionary-style access (config["llm"]["groq"], etc.).
    """
    def __init__(self):
        print("Loaded config.....")
        self.config = load_config()   # Load the YAML configuration
    
    def __getitem__(self, key):
        # Enables config["llm"] style access
        return self.config[key]


# ------------------------------
# Model Loader Class
# ------------------------------
class ModelLoader(BaseModel):
    """
    Loads an LLM (either Groq or OpenAI) based on the configuration.
    Uses Pydantic BaseModel for type safety and validation.
    """
    # Which provider to use ("groq" or "openai")
    model_provider: Literal["groq", "openai"] = "groq"

    # Config loader instance (not included in JSON serialization/export)
    config: Optional[ConfigLoader] = Field(default=None, exclude=True)

    # Pydantic lifecycle hook - runs after model initialization
    def model_post_init(self, __context: Any) -> None:
        # Automatically load the config once the class is created
        self.config = ConfigLoader()
    
    class Config:
        # Allow non-Pydantic objects inside this model (like ConfigLoader)
        arbitrary_types_allowed = True
    
    # --------------------------
    # Load the selected LLM
    # --------------------------
    def load_llm(self):
        """
        Load and return the LLM model (Groq or OpenAI).
        API keys are taken from environment variables.
        Model names are read from config.yaml.
        """
        print("LLM loading...")
        print(f"Loading model from provider: {self.model_provider}")

        # --------------------------
        # If Groq provider selected
        # --------------------------
        if self.model_provider == "groq":
            print("Loading LLM from Groq..............")
            groq_api_key = os.getenv("GROQ_API_KEY")   # load from .env
            model_name = self.config["llm"]["groq"]["model"]  # from config.yaml
            llm = ChatGroq(model=model_name, api_key=groq_api_key)

        # --------------------------
        # If OpenAI provider selected
        # --------------------------
        elif self.model_provider == "openai":
            print("Loading LLM from OpenAI..............")
            openai_api_key = os.getenv("OPENAI_API_KEY")   # load from .env
            model_name = self.config["llm"]["openai"]["model"]  # from config.yaml
            llm = ChatOpenAI(model=model_name, api_key=openai_api_key)
        
        # Return the loaded LLM object
        return llm
