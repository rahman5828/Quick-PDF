from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from app.routes.merge import router as merge_router

app = FastAPI(title="Quick-PDF", version="2.0.0")

# Routes
app.include_router(merge_router)

# Serve static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Home page
@app.get("/", response_class=HTMLResponse)
async def home():
    with open("app/static/index.html", "r", encoding="utf-8") as f:
        return f.read()

# Health check
@app.get("/health")
def health():
    return {"status": "ok"}

# Version
@app.get("/version")
def version():
    return {"version": "2.0.0"}
