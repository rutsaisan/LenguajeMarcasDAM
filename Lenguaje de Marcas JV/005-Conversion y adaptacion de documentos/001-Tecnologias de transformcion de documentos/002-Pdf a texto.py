# pip3 install pypdf --break-system-packages  Linux
# pip install pypdf                           Windows
from pypdf import PdfReader

lector = PdfReader("librophp.pdf")
texto = ""

for pagina in lector.pages:
    texto += pagina.extract_text() + "\n"

print(texto)