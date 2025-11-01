from langchain_groq import ChatGroq
from app.config import settings

def get_model(tools):
    model = ChatGroq(model_name=settings.MODEL_NAME, groq_api_key=settings.GROQ_API_KEY)
    return model.bind_tools(tools)