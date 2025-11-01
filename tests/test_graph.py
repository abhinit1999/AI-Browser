from app.tools import get_tools
from app.model import get_model
from app.graph import build_graph
from langchain_core.messages import HumanMessage

def test_graph_response():
    tools = get_tools()
    llm_with_tools = get_model(tools)
    graph = build_graph(llm_with_tools, tools)

    query = "Is 'Attention is All You Need' a research paper?"
    result = graph.invoke({"messages": [HumanMessage(content=query)]})

    assert "messages" in result
    assert isinstance(result["messages"], list)
    assert any(msg.content for msg in result["messages"])