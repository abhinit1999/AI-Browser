from fastapi import APIRouter
from langchain_core.messages import HumanMessage
from app.tools import get_tools
from app.model import get_model
from app.graph import build_graph

router = APIRouter()

tools = get_tools()
llm_with_tools = get_model(tools)
graph = build_graph(llm_with_tools, tools)

@router.get("/")
def Home():
    return {"message":"THis is the Home page of AI Browser"}
@router.post("/query")
def query_graph(payload: dict):
    user_input = payload.get("message", "")
    result = graph.invoke({"messages": [HumanMessage(content=user_input)]})
    return {"response": [msg.content for msg in result["messages"]]}