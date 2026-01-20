from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pypdf import PdfMerger
import tempfile
import os
from datetime import datetime

# -------------------------
# App config
# -------------------------
APP_NAME = "Quick-PDF"
APP_VERSION = "2.0.0"

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION
)

# -------------------------
# Static & templates
# -------------------------
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# -------------------------
# UI Home
# -------------------------
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

# -------------------------
# Merge PDFs
# -------------------------
@app.post("/merge")
async def merge_pdfs(
    pdf1: UploadFile = File(...),
    pdf2: UploadFile = File(...)
):
    merger = PdfMerger()
    temp_files = []

    try:
        for pdf in [pdf1, pdf2]:
            tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
            tmp.write(await pdf.read())
            tmp.close()
            temp_files.append(tmp.name)
            merger.append(tmp.name)

        output_path = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf").name
        merger.write(output_path)
        merger.close()

        return FileResponse(
            output_path,
            media_type="application/pdf",
            filename="merged.pdf"
        )

    finally:
        for path in temp_files:
            if os.path.exists(path):
                os.remove(path)

# -------------------------
# Health check
# -------------------------
@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": APP_NAME,
        "time": datetime.utcnow().isoformat()
    }

# -------------------------
# Version info
# -------------------------
@app.get("/version")
def version():
    return {
        "app": APP_NAME,
        "version": APP_VERSION
    }
