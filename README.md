# Smart Document Reader – Task A

A document extraction system supporting:
✔ Bank statements
✔ Loan agreements
✔ OCR extraction (Tesseract)
✔ PDF → Image (Poppler)
✔ LLM extraction fallback
✔ Document classifier
✔ FastAPI backend
✔ SQLite storage

## Setup (Windows)

1. Install Python 3.10+
2. Install Tesseract:
   https://github.com/UB-Mannheim/tesseract/wiki
3. Install Poppler:
   https://github.com/oschwartz10612/poppler-windows/releases/

Ensure paths:
C:\Program Files\Tesseract-OCR\tesseract.exe
C:\poppler\Library\bin\pdftoppm.exe

4. Create and activate venv:
python -m venv venv
.\venv\Scripts\Activate.ps1

5. Install dependencies:
pip install -r requirements.txt

## Run server
python -m uvicorn main:app --reload --port 8000

Open:
http://127.0.0.1:8000/docs

Upload any PDF:
- 12-month statement
- Loan agreement
- Simple statement

