from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.routes.merge import router as merge_router

app = FastAPI(
    title="Quick-PDF",
    description="Fast, Secure PDF tools",
    version="2.0.0"
)

# API routes
app.include_router(merge_router)

# Serve static UI
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Serve UI at root
@app.get("/")
def serve_ui():
    return FileResponse("app/static/index.html")
