from fastapi import FastAPI
from app.routes.merge import router as merge_router

app = FastAPI(title="Quick-PDF")

app.include_router(merge_router)

@app.get("/")
def home():
    return {"status": "Quick-PDF backend running 🚀"}
