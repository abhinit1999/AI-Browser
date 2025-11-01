from app.tools import get_tools

def test_tools_setup():
    tools = get_tools()
    assert len(tools) == 3