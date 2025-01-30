from PyPDF2 import PdfReader
from pathlib import Path
from PIL import Image
import os

ROOT_PATH = Path(__file__).parent
PDF_FILE_PATH = Path(os.path.join(ROOT_PATH, "pdfs_originais\R20250124.pdf"))
NEW_PDFS_FOLDER = Path(os.path.join(ROOT_PATH, "novos_pdfs"))

# cria uma pasta nova na raiz para alocar novos pdfs, caso necessário.
NEW_PDFS_FOLDER.mkdir(exist_ok=True)

# criando um novo leitor de PDFs
reader = PdfReader(PDF_FILE_PATH)
print("Este PDF possui", len(reader.pages), "páginas")

first_page = reader.pages[0]

# extrai o texto de uma página específica (PageObject)
print(first_page.extract_text())


# TextIOWrapper -> gerenciador de contextos que estabele uma conexão com um arquivo especificado
# e inicializa um objeto capaz de representá-lo. Também é reponsável por finalizar a conexão com o arquivo.

# TextIO -> representação do arquivo na forma de um objeto python

