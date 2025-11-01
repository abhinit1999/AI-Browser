from app.tools import get_tools
from app.model import get_model

def test_model_binding():
    tools = get_tools()
    llm_with_tools = get_model(tools)

    assert hasattr(llm_with_tools, "invoke")
    assert callable(llm_with_tools.invoke)
    assert llm_with_tools.model_name == "openai/gpt-oss-20b"