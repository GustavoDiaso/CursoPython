from PIL import Image
from pathlib import Path

ROOT_FOLDER_PATH = Path(__file__).parent
ORIGINAL_IMAGE_PATH = ROOT_FOLDER_PATH / "imagem_random.jpg"
MODIFIED_IMAGE_PATH = ROOT_FOLDER_PATH / "imagem_modificada.jpg"

original_image = Image.open(ORIGINAL_IMAGE_PATH)
width, height = original_image.size

new_width = width - 300
new_height = height - 300

# o método resize retora uma cópia da imagem original seguindo as predefinições passadas nos argumentos
new_image = original_image.resize(size=(new_width, new_height))
new_image.save(
    fp=MODIFIED_IMAGE_PATH,
    format=None,
    optimize=True,
)
