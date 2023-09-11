from my_toolkit import HouseSearchToolkit

def test_toolkit_initialization():
    toolkit = HouseSearchToolkit()
    
    # Check if toolkit has the correct name
    assert toolkit.name == "House Search Toolkit", f"Expected 'House Search Toolkit', but got {toolkit.name}"

    # Check if toolkit returns the correct tools
    tools = toolkit.get_tools()
    assert len(tools) == 1, f"Expected 1 tool, but got {len(tools)}"
    assert isinstance(tools[0], HouseSearchTool), f"Expected HouseSearchTool, but got {type(tools[0])}"

    # Check environment keys
    env_keys = toolkit.get_env_keys()
    assert "OPENAI_KEY" in env_keys, "OPENAI_KEY not found in environment keys"
    assert "PROPGPT_API_KEY" in env_keys, "PROPGPT_API_KEY not found in environment keys"
