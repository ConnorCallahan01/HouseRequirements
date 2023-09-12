from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type, List
import requests

# Define the input model
class HouseRequirements(BaseModel):
    query: str = Field(..., description="Natural language query for house requirements")

# Define the custom tool
class HouseSearchTool(BaseTool):
    name: str = "House Search Tool"
    args_schema: Type[BaseModel] = HouseRequirements
    description: str = "Searches for houses based on given requirements using PropGPT API"
    
    def _execute(self, query: str) -> List[str]:
        # Define the PropGPT API endpoint
        endpoint = "https://api.realestateapi.com/v2/PropGPT"
        
        # Define the headers
        headers = {
            'accept': 'text/plain',
            'content-type': 'application/json',
            'x-openai-key': self.get_tool_config('OPENAI_KEY'),  # Replace with your OpenAI key
            'x-api-key': self.get_tool_config('PROPGPT_API_KEY')  # Replace with your PropGPT API key
        }
        
        # Make the POST request
        response = requests.post(endpoint, headers=headers, json={"query": query})
        
        # Process the response and return
        if response.status_code == 200:
            return response.text
        else:
            return ["Error occurred while fetching data from PropGPT API"]
