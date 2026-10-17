import fitz  # PyMuPDF

pdf_path = "data/raw/world_bank/education/secondary_education/dropout/WB_PODER_Mexico_2019.pdf"

document = fitz.open(pdf_path)

full_text = ""

for page_number, page in enumerate(document, start=1):
    text = page.get_text()
    full_text += f"\n--- PAGE {page_number} ---\n"
    full_text += text

print("Número de páginas:", len(document))
print()
print("Primeiros 3000 caracteres do documento:")
print()
print(full_text[:3000])
