from PyPDF2 import PdfWriter, PdfReader
from pathlib import Path
from PIL import Image
import os

ROOT_PATH = Path(__file__).parent
PDF_FILE_PATH = Path(os.path.join(ROOT_PATH, "pdfs_originais\R20250124.pdf"))
NEW_PDFS_FOLDER = Path(os.path.join(ROOT_PATH, "novos_pdfs"))

# cria uma pasta nova na raiz para alocar novos pdfs, caso necessário.
NEW_PDFS_FOLDER.mkdir(exist_ok=True)

reader = PdfReader(PDF_FILE_PATH)
writer = PdfWriter()

# para cada página no nosso pdf
for i, page in enumerate(reader.pages):
    # adiciona uma nova página ao objeto PdfWriter
    writer.add_page(page)

# TextIOWrapper -> gerenciador de contextos que estabele uma conexão com um arquivo especificado, interpreta o arquivo
# e inicializa um objeto capaz de representá-lo. Também é reponsável por analisar as modificações feitas no objeto
# IO e aplicá-las no arquivo original, finalizando a conexão logo em seguida.

with open(os.path.join(NEW_PDFS_FOLDER, "R20250124_modified.pdf"), "wb") as arquivo:
    # Escreve todas as páginas adicionadas ao objeto PdfWriter no arquivo especificado.
    writer.write(arquivo)


# Separando as páginas do PDF orinal...
for i, page in enumerate(reader.pages):
    new_writer = PdfWriter()
    new_writer.add_page(page)
    with open(
        os.path.join(NEW_PDFS_FOLDER, f"R20250124_pagina{i+1}.pdf"), "wb"
    ) as arquivo:
        new_writer.write(arquivo)
