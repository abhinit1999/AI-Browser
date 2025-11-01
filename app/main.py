from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="LangChain Tool Graph API")
app.include_router(router)