from PyPDF2 import PdfReader, PdfMerger
from pathlib import Path
from PIL import Image
import os

ROOT_PATH = Path(__file__).parent
PDF_FILE_PATH = Path(os.path.join(ROOT_PATH, "pdfs_originais\R20250124.pdf"))
NEW_PDFS_FOLDER = Path(os.path.join(ROOT_PATH, "novos_pdfs"))

# cria uma pasta nova na raiz para alocar novos pdfs, caso necessário.
NEW_PDFS_FOLDER.mkdir(exist_ok=True)

path_files = [
    os.path.join(NEW_PDFS_FOLDER, "R20250124_pagina1.pdf"),
    os.path.join(NEW_PDFS_FOLDER, "R20250124_pagina1.pdf"),
]
merger = PdfMerger()

for file_path in path_files:
    merger.append(file_path)


MERGED_PDF_PATH = Path(os.path.join(NEW_PDFS_FOLDER, "MERGED_PDF.pdf"))

with open(MERGED_PDF_PATH, "wb") as merged_pdf:
    merger.write(merged_pdf)
