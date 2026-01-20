from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from app.routes.merge import router as merge_router

# -------------------------------------------------
# App initialization
# -------------------------------------------------
app = FastAPI(
    title="Quick-PDF",
    description="Fast • Secure • World-Class PDF Tools",
    version="2.0.0"
)

# -------------------------------------------------
# Static files (CSS, JS)
# -------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent

app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static"
)

# -------------------------------------------------
# Routes
# -------------------------------------------------
app.include_router(merge_router)


# -------------------------------------------------
# Home UI
# -------------------------------------------------
@app.get("/", response_class=HTMLResponse)
def home():
    html_path = BASE_DIR / "static" / "index.html"
    return html_path.read_text(encoding="utf-8")


# -------------------------------------------------
# Version endpoint (PRODUCTION STANDARD)
# -------------------------------------------------
@app.get("/version")
def version():
    return {
        "name": "Quick-PDF",
        "version": "2.0.0",
        "environment": "production",
        "ui": "v2-dark",
        "stack": ["FastAPI", "Docker", "AWS EC2"]
    }


# -------------------------------------------------
# Health check (optional but professional)
# -------------------------------------------------
@app.get("/health")
def health():
    return {"status": "ok"}
