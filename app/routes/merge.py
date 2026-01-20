from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse
from typing import List
from pypdf import PdfReader, PdfWriter
import tempfile
import shutil
import os

router = APIRouter()

@router.post("/merge")
async def merge_pdfs(files: List[UploadFile] = File(...)):
    writer = PdfWriter()
    temp_input_files = []

    # 1. Save uploaded PDFs
    for uploaded_file in files:
        temp_pdf = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
        with open(temp_pdf.name, "wb") as buffer:
            shutil.copyfileobj(uploaded_file.file, buffer)
        temp_input_files.append(temp_pdf.name)

    # 2. Read PDFs SAFELY (close files properly)
    for path in temp_input_files:
        with open(path, "rb") as f:
            reader = PdfReader(f)
            for page in reader.pages:
                writer.add_page(page)

    # 3. Write merged PDF
    output_pdf = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    writer.write(output_pdf.name)
    writer.close()

    # 4. Cleanup input temp files (now safe)
    for path in temp_input_files:
        try:
            os.remove(path)
        except PermissionError:
            pass  # Windows safety

    return FileResponse(
        path=output_pdf.name,
        filename="merged.pdf",
        media_type="application/pdf"
    )
