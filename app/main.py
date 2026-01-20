from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from app.routes.merge import router as merge_router

# -------------------------------------------------
# App init
# -------------------------------------------------
app = FastAPI(
    title="Quick-PDF",
    description="Fast • Secure • World-Class PDF Tools",
    version="2.0.0"
)

BASE_DIR = Path(__file__).resolve().parent

# -------------------------------------------------
# Static files
# -------------------------------------------------
app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static"
)

# -------------------------------------------------
# API ROUTES (FIRST)
# -------------------------------------------------
app.include_router(merge_router)


@app.get("/version")
def version():
    return {
        "name": "Quick-PDF",
        "version": "2.0.0",
        "environment": "production",
        "ui": "v2",
        "stack": ["FastAPI", "Docker", "AWS EC2"]
    }


@app.get("/health")
def health():
    return {"status": "ok"}


# -------------------------------------------------
# UI ROUTE (LAST – VERY IMPORTANT)
# -------------------------------------------------
@app.get("/", response_class=HTMLResponse)
def home():
    return (BASE_DIR / "static" / "index.html").read_text(encoding="utf-8")
