import pytest
from my_tool import HouseSearchTool, HouseRequirements

def test_valid_query():
    tool = HouseSearchTool()
    query = "3-bedroom house in San Francisco with a garden"
    results = tool._execute(query=query)
    
    # Check if the result is a list (as expected)
    assert isinstance(results, list), f"Expected a list, but got {type(results)}"

    # Check if there's an error message in the results
    assert "Error occurred" not in results[0], f"Error: {results[0]}"

def test_invalid_query():
    tool = HouseSearchTool()
    query = ""  # Empty query
    results = tool._execute(query=query)
    
    # Check if an error message is returned
    assert "Error occurred" in results[0], f"Expected an error, but got: {results[0]}"
