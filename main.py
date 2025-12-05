from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import uuid, shutil, json
from pathlib import Path

from ocr_utils import pdf_to_images, image_ocr_text
from extractor import extract_fields
from classifier import classify_document
from db import init_db, save_result

app = FastAPI(title="Smart Document Reader - Task A")

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

DB_PATH = "results.db"
init_db(DB_PATH)


@app.post("/api/verify")
async def verify(file: UploadFile = File(...)):
    uid = uuid.uuid4().hex
    dest = DATA_DIR / f"{uid}_{file.filename}"

    # Save file
    with open(dest, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # 1) Convert PDF → images
    try:
        images = pdf_to_images(dest)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"PDF conversion error: {e}")

    # 2) OCR text extraction
    full_text = ""
    for img in images:
        full_text += image_ocr_text(img) + "\n"

    # 3) Document Classification (loan / statement)
    doc_type, doc_conf = classify_document(full_text)

    # 4) Field Extraction (Hybrid: Rules + LLM fallback)
    extracted, confidence = extract_fields(full_text)

    result = {
        "id": uid,
        "docType": doc_type,
        "docTypeConfidence": doc_conf,
        "file": str(dest),
        "extracted": extracted,
        "confidence": confidence,
        "text_snippet": full_text[:2000]
    }

    save_result(DB_PATH, result)
    (DATA_DIR / f"{uid}_result.json").write_text(json.dumps(result, indent=2))

    return JSONResponse(content=result)
