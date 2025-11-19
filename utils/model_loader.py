import os
from dotenv import load_dotenv
load_dotenv()
from typing import Any, Literal, Optional
from pydantic import BaseModel, Field 
from utils.config_loader import load_config
#from langchain_groq import ChatGroq
from google import genai
from langchain_google_genai import ChatGoogleGenerativeAI


class ConfigLoader:
    def __init__(self):
        print(f"Loaded config.....")
        self.config = load_config()

    def __getitem__(self, key):
        return self.config[key]

class ModelLoader(BaseModel):
    model_provider: Literal["genai"] = "genai"
    config: Optional[ConfigLoader] = Field(default=None, exclude=True)

    def model_post_init(self, __context: Any) -> None:
        self.config = ConfigLoader()

    class Config:
        arbitrary_types_allowed = True
    
    def load_llm(self):
        """
        Load and return the LLM model.
        """
        print("LLM loading...")
        print(f"loading model from provider: {self.model_provider}")
        self.model_provider == "genai"
        print("Loading LLM from Gemini...........")
        #groq_api_key = os.getenv("GROQ_API_KEY")
        google_api_key = os.getenv("GOOGLE_API_KEY")
        model_name = self.config["llm"]["genai"]["model_name"]
        llm = ChatGoogleGenerativeAI(model = model_name, api_key = google_api_key)

        return llm