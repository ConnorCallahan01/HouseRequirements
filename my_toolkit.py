from superagi.tools.base_tool import BaseToolkit, BaseTool
from typing import Type, List

class HouseSearchToolkit(BaseToolkit):
    name: str = "House Search Toolkit"
    description: str = "Toolkit for searching houses using PropGPT API"
    
    def get_tools(self) -> List[BaseTool]:
        return [HouseSearchTool()]
    
    def get_env_keys(self) -> List[str]:
        return ['OPENAI_KEY', 'PROPGPT_API_KEY']