from superagi.tools.base_tool import BaseToolkit, BaseTool, ToolConfiguration
from typing import Type, List
from superagi.tools.external_tools.HouseRequirements.my_tool import HouseSearchTool
from superagi.models.tool_config import ToolConfig
from superagi.types.key_type import ToolConfigKeyType


class HouseSearchToolkit(BaseToolkit):
    name: str = "House Search Toolkit"
    description: str = "Toolkit for searching houses using PropGPT API"
    
    def get_tools(self) -> List[BaseTool]:
        return [HouseSearchTool()]
    
    
    def get_env_keys(self) -> List[ToolConfiguration]:
        return [
            ToolConfiguration(key='OPENAI_KEY', key_type=ToolConfigKeyType.STRING, is_required= True, is_secret = True),
            ToolConfiguration(key='PROPGPT_API_KEY', key_type=ToolConfigKeyType.STRING, is_required= True, is_secret = True)
        ]
