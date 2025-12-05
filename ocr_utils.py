from pdf2image import convert_from_path
from PIL import Image
import pytesseract
from pathlib import Path

# Tesseract path (check with: where tesseract)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Poppler path (ensure pdftoppm.exe is inside this folder)
POPPLER_PATH = r"C:\poppler\Library\bin"

def pdf_to_images(path):
    p = Path(path)
    if p.suffix.lower() == ".pdf":
        return convert_from_path(str(p), dpi=300, poppler_path=POPPLER_PATH)
    else:
        return [Image.open(p).convert("RGB")]

def image_ocr_text(img):
    return pytesseract.image_to_string(img, lang="eng")
